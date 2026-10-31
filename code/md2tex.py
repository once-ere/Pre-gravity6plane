#!/usr/bin/env python3
r"""md2tex.py -- convert the restricted GitHub-Markdown used in this repository to a standalone LaTeX file.
Supported: # headings, paragraphs, **bold**, *italic*, `code`, [links](url), inline math $..$, display math $$..$$,
'-'/'*' bullet lists, '1.' numbered lists, ``` code blocks, indented code blocks, '>' quotes, '|' tables, '---' rules,
<!-- comments --> (kept as LaTeX comments), <span style="font-size: Npx;"> (scaled by 10pt/16px), backslash escapes of
ASCII punctuation, hard line breaks (two trailing spaces).  As on GitHub, a paragraph that is one $$..$$ is displayed and
a $$..$$ inside a paragraph is set inline in display style.  In math, \\{ and \\} become \{ and \} and the MathJax macro
\space becomes '\ '.  Straight quotes become opening/closing quotes, judged from their neighbours.  The first # heading
is the title; later # headings are unnumbered sections in the title's size.  Text and table cells are set ragged right,
as GitHub sets them.  Usage: md2tex.py in.md out.tex"""
import re, sys
UNI = {'\u2013': '--', '\u2014': '---', '\u2019': "'", '\u2018': '`', '\u201c': '``', '\u201d': "''", '\u00d7': r'$\times$',
       '\u00b1': r'$\pm$', '\u2192': r'$\to$', '\u2264': r'$\le$', '\u2265': r'$\ge$', '\u2260': r'$\neq$', '\u00b7': r'$\cdot$',
       '\u2026': r'\ldots{}', '\u00a0': '~', '\u2212': '-', '\u2248': r'$\approx$', '\u221e': r'$\infty$',
       '\u00b0': r'\textdegree{}', '\u00f8': r'{\o}'}
MATHUNI = {k: v.strip('$') for k, v in UNI.items() if v.startswith('$')}
MATHUNI.update({'\u2212': '-', '\u00b0': r'^\circ'})
ESC0 = 0xE000                       # chr(ESC0 + ord(c)) stands for the backslash-escaped punctuation character c
BR = '\uE100'                       # hard line break
LIT = {'\\': r'\textbackslash{}', '^': r'\^{}', '~': r'\~{}', '<': r'\textless{}', '>': r'\textgreater{}',
       "'": r'\textquotesingle{}', '"': r'\textquotedbl{}', '`': r'\textasciigrave{}', '-': '-{}'}
def lit(ch):
    # LaTeX for a backslash-escaped (literal) punctuation character
    return LIT.get(ch, '\\' + ch if ch in '{}#%&_$' else ch)
def unesc(ch):
    return chr(ord(ch) - ESC0) if ESC0 < ord(ch) <= ESC0 + 0x7E else ch
def esc_code(t):
    out = []
    for ch in t:
        if ch == '\\': out.append(r'\textbackslash{}')
        elif ch in '{}#%&_$': out.append('\\' + ch)
        elif ch == '^': out.append(r'\^{}')
        elif ch == '~': out.append(r'\~{}')
        elif ch == '<': out.append(r'\textless{}')
        elif ch == '>': out.append(r'\textgreater{}')
        elif ch in UNI: out.append(UNI[ch])
        elif ord(ch) > 127: raise ValueError('non-ASCII character %r in text: %r' % (ch, t))
        else: out.append(ch)
    return ''.join(out)
def esc(t, prev=' ', nxt=' '):
    # prev/nxt: the characters just outside t, used to tell opening quotes from closing quotes
    out, popen = [], False
    for k, ch in enumerate(t):
        p = unesc(t[k - 1] if k else prev); q = unesc(t[k + 1] if k + 1 < len(t) else nxt)
        if ch in '\'"':
            op = (p.isspace() or p in '([{' or popen) and not q.isspace()
            s = ('`' if op else "'") * (1 if ch == "'" else 2)
            if out and out[-1][-1:] in ('`', "'"): s = '{}' + s
            out.append(s); popen = op; continue
        popen = False
        if ch == '\\': out.append(r'\textbackslash{}')
        elif ch in '{}#%&_$': out.append('\\' + ch)
        elif ch == '^': out.append(r'\^{}')
        elif ch == '~': out.append(r'\~{}')
        elif ch == '<': out.append(r'\textless{}')
        elif ch == '>': out.append(r'\textgreater{}')
        elif ch == '-' and q == '-': out.append('-{}')
        elif ch == BR: out.append(r'\newline ')
        elif unesc(ch) != ch: out.append(ch)                # resolved by fmt_text after the emphasis markup
        elif ch in UNI: out.append(UNI[ch])
        elif ord(ch) > 127: raise ValueError('non-ASCII character %r in text: %r' % (ch, t))
        else: out.append(ch)
    return ''.join(out)
def fmt_text(t, prev=' ', nxt=' '):
    t = esc(t, prev, nxt)
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\\emph{\1}', t)
    return re.sub('[\uE021-\uE07E]', lambda m: lit(unesc(m.group(0))), t)
def mathnorm(t):
    t = t.replace('\\\\{', '\\{').replace('\\\\}', '\\}')
    t = re.sub(r'\\space(?![A-Za-z])', r'\\ ', t)
    for k, v in MATHUNI.items(): t = t.replace(k, v)
    t = t.replace(BR, ' ')
    if any(ord(c) > 127 for c in t): raise ValueError('non-ASCII in math: %r' % t)
    return t
TOK = re.compile(r'(?P<esc>\\[!-/:-@\[-`{-~])|(?P<code>`[^`]+?`)|(?P<dm>\$\$.+?\$\$)|(?P<m>\$[^$]+?\$)'
                 r'|(?P<link>\[(?P<lt>[^\]]+)\]\((?P<lu>[^)]+)\))'
                 r'|(?P<html></?[A-Za-z][A-Za-z0-9-]*(?:\s+[A-Za-z_:][\w.:-]*(?:\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^\s"\'=<>`]+))?)*\s*/?>)', re.S)
def inline(s):
    # split into backslash escapes, code `..`, math $$..$$ and $..$, links [..](..), raw HTML tags, and text
    segs, i, depth = [], 0, 0                  # segs: [kind, source, payload]
    def text(src, pay):
        if segs and segs[-1][0] == 't': segs[-1][1] += src; segs[-1][2] += pay
        else: segs.append(['t', src, pay])
    for m in TOK.finditer(s):
        if m.start() > i: text(s[i:m.start()], s[i:m.start()])
        g = m.group(0)
        if m.group('esc'): text(g, chr(ESC0 + ord(g[1])))
        elif m.group('code'): segs.append(['x', g, r'\texttt{' + esc_code(g[1:-1]) + '}'])
        elif m.group('dm'): segs.append(['x', g, r'$\displaystyle ' + mathnorm(g[2:-2]) + '$'])
        elif m.group('m'): segs.append(['x', g, '$' + mathnorm(g[1:-1]) + '$'])
        elif m.group('link'):
            segs.append(['x', g, r'\href{' + m.group('lu').replace('%', r'\%').replace('#', r'\#') + '}{' + fmt_text(m.group('lt')) + '}'])
        else:
            fs = re.fullmatch(r'<span style="font-size:\s*([\d.]+)px;?">', g)
            if fs:
                pt = float(fs.group(1)) * 10 / 16; depth += 1
                segs.append(['open', g, r'{\fontsize{%g}{%g}\selectfont ' % (pt, 1.2 * pt)])
            elif g == '</span>' and depth > 0: depth -= 1; segs.append(['x', g, '}'])
            else: raise ValueError('unsupported HTML tag %r in: %r' % (g, s))
        i = m.end()
    if i < len(s): text(s[i:], s[i:])
    if depth: raise ValueError('unclosed <span> in: %r' % s)
    res = []
    for k, (kind, src, pay) in enumerate(segs):
        if kind != 't': res.append(pay); continue
        prev = ' ' if k == 0 or segs[k - 1][0] == 'open' else segs[k - 1][1][-1]
        nxt = segs[k + 1][1][0] if k + 1 < len(segs) else ' '
        res.append(fmt_text(pay, prev, nxt))
    return ''.join(res)
def split_row(line):
    # split a markdown table row on '|' that are not inside $...$ math
    cells, cur, inmath = [], '', False
    body = line.strip()
    if body.startswith('|'): body = body[1:]
    if body.endswith('|'): body = body[:-1]
    for ch in body:
        if ch == '$': inmath = not inmath
        if ch == '|' and not inmath: cells.append(cur.strip()); cur = ''
        else: cur += ch
    cells.append(cur.strip()); return cells
PRE = r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=1.7cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb}
\usepackage{longtable,booktabs,array}
\usepackage{listings}
\usepackage[hidelinks]{hyperref}
\lstset{basicstyle=\ttfamily\footnotesize,breaklines=true,columns=fullflexible,keepspaces=true,upquote=true}
\setcounter{MaxMatrixCols}{20}
\allowdisplaybreaks
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}\setlength{\emergencystretch}{3em}\sloppy\raggedright
\begin{document}
"""
MDPART = r"""\makeatletter
\newcommand\mdpart{\@startsection{section}{1}{\z@}{-3.5ex \@plus -1ex \@minus -.2ex}{2.3ex \@plus.2ex}{\normalfont\LARGE\bfseries\raggedright}}
\makeatother
"""
def convert(md):
    lines = md.split('\n'); out = [PRE]; i = 0; n = len(lines); title = False; part = False
    def flush_list(stack):
        while stack: out.append(r'\end{' + stack.pop() + '}')
    liststack = []
    while i < n:
        l = lines[i]
        if l.strip().startswith('```'):
            flush_list(liststack); i += 1; buf = []
            while i < n and not lines[i].strip().startswith('```'): buf.append(lines[i]); i += 1
            for b in buf:
                if any(ord(c) > 127 for c in b): raise ValueError('non-ASCII in code block: ' + b)
            out.append(r'\begin{lstlisting}' + '\n' + '\n'.join(buf) + '\n' + r'\end{lstlisting}'); i += 1; continue
        if l.strip() == '$$':
            flush_list(liststack); i += 1; buf = []
            while i < n and lines[i].strip() != '$$': buf.append(lines[i]); i += 1
            out.append(r'\[' + '\n' + mathnorm('\n'.join(buf)) + '\n' + r'\]'); i += 1; continue
        if re.match(r'^ {4,}\S', l):
            # indented code block: runs of 4-space-indented and blank lines; trailing blank lines are not part of it
            flush_list(liststack); buf = []
            while i < n and (lines[i].startswith('    ') or not lines[i].strip()): buf.append(lines[i][4:].rstrip()); i += 1
            while not buf[-1]: buf.pop(); i -= 1
            for b in buf:
                if any(ord(c) > 127 for c in b): raise ValueError('non-ASCII in code block: ' + b)
            out.append(r'\begin{lstlisting}' + '\n' + '\n'.join(buf) + '\n' + r'\end{lstlisting}'); continue
        if re.match(r'^ {0,3}<!--', l):
            # HTML comment: not displayed by GitHub, kept as LaTeX comment lines
            flush_list(liststack)
            while True:
                out.append('% ' + lines[i]); i += 1
                if '-->' in lines[i - 1] or i == n: break
            if not lines[i - 1].rstrip().endswith('-->'): raise ValueError('text after an HTML comment: ' + lines[i - 1])
            continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            flush_list(liststack); lev = len(m.group(1)); txt = inline(re.sub(r'\s+#+\s*$', '', m.group(2)).strip())
            if lev == 1 and not title: out.append(r'{\raggedright\LARGE\bfseries ' + txt + r'\par}\medskip'); title = True
            elif lev == 1: out.append(r'\mdpart*{' + txt + '}'); part = True
            else: out.append({2: r'\section*{', 3: r'\subsection*{', 4: r'\subsubsection*{'}[lev] + txt + '}')
            i += 1; continue
        if l.strip() == '---':
            flush_list(liststack); out.append(r'\par\noindent\rule{\linewidth}{0.4pt}\par'); i += 1; continue
        if l.startswith('|'):
            flush_list(liststack); rows = []
            while i < n and lines[i].startswith('|'):
                if not re.match(r'^\|\s*:?-{2,}', lines[i]): rows.append(split_row(lines[i]))
                i += 1
            nc = max(len(r) for r in rows); w = 0.96 / nc
            colw = r'>{\raggedright\arraybackslash}p{\dimexpr %.4f\linewidth-2\tabcolsep\relax}' % w
            out.append(r'{\small\begin{longtable}{' + colw * nc + '}\\toprule')
            for k, r in enumerate(rows):
                out.append(' & '.join(inline(c) for c in r + [''] * (nc - len(r))) + r' \\' + (r'\midrule' if k == 0 else ''))
            out.append(r'\bottomrule\end{longtable}}'); continue
        if l.startswith('> '):
            flush_list(liststack); buf = []
            while i < n and lines[i].startswith('>'): buf.append(lines[i][1:].strip()); i += 1
            out.append(r'\begin{quote}' + inline(' '.join(buf)) + r'\end{quote}'); continue
        mb = re.match(r'^(\s*)[-*]\s+(.*)$', l); mn = re.match(r'^(\s*)\d+\.\s+(.*)$', l)
        if mb or mn:
            kind = 'itemize' if mb else 'enumerate'; m2 = mb or mn
            depth = len(m2.group(1)) // 2 + 1
            while len(liststack) < depth: out.append(r'\begin{' + kind + '}'); liststack.append(kind)
            while len(liststack) > depth: out.append(r'\end{' + liststack.pop() + '}')
            if liststack[-1] != kind: out.append(r'\end{' + liststack.pop() + '}'); out.append(r'\begin{' + kind + '}'); liststack.append(kind)
            item = m2.group(2); i += 1
            while i < n and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'^\s*([-*]|\d+\.)\s+', lines[i]) and lines[i].strip() != '$$':
                item += ' ' + lines[i].strip(); i += 1
            out.append(r'\item ' + inline(item)); continue
        if l.strip() == '':
            flush_list(liststack); out.append(''); i += 1; continue
        flush_list(liststack); buf = [l]; i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(('#', '|', '>', '```', '<!--')) and lines[i].strip() != '$$' and not re.match(r'^\s*([-*]|\d+\.)\s+', lines[i]) and lines[i].strip() != '---':
            buf.append(lines[i]); i += 1
        sl = [b.strip() for b in buf]
        dm = re.fullmatch(r'\$\$(.+?)\$\$', '\n'.join(sl), flags=re.S)
        if dm and '$$' not in dm.group(1): out.append(r'\[' + mathnorm(dm.group(1)) + r'\]'); continue
        para = ' '.join(s + (BR if b.endswith('  ') and k < len(buf) - 1 else '') for k, (s, b) in enumerate(zip(sl, buf)))
        sp = re.fullmatch(r'<span style="font-size:\s*[\d.]+px;?">(.*)</span>', para, flags=re.S)
        if sp and '<span' not in sp.group(1) and '</span>' not in sp.group(1):
            # a paragraph that is one sized span ends inside the span, so its own line spacing applies
            out.append(inline(para)[:-1] + r'\par}' + '\n'); continue
        out.append(inline(para) + '\n')
    flush_list(liststack); out.append(r'\end{document}')
    if part: out[0] = PRE.replace(r'\begin{document}', MDPART + r'\begin{document}')
    return '\n'.join(out)
if __name__ == '__main__':
    src = open(sys.argv[1], encoding='utf-8').read()
    open(sys.argv[2], 'w', encoding='ascii').write(convert(src))
