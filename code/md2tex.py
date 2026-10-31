#!/usr/bin/env python3
"""md2tex.py -- convert the restricted GitHub-Markdown used in this repository to a standalone LaTeX file.
Supported: # headings, paragraphs, **bold**, *italic*, `code`, [links](url), inline math $..$, display math $$..$$,
'-' bullet lists, '1.' numbered lists, ``` code blocks, '>' quotes, '|' tables, '---' rules.  Usage: md2tex.py in.md out.tex"""
import re, sys
UNI = {'\u2013': '--', '\u2014': '---', '\u2019': "'", '\u2018': '`', '\u201c': '``', '\u201d': "''", '\u00d7': r'$\times$',
       '\u00b1': r'$\pm$', '\u2192': r'$\to$', '\u2264': r'$\le$', '\u2265': r'$\ge$', '\u2260': r'$\neq$', '\u00b7': r'$\cdot$',
       '\u2026': r'\ldots{}', '\u00a0': '~', '\u2212': '-', '\u2248': r'$\approx$', '\u221e': r'$\infty$'}
def esc(t):
    out = []
    for ch in t:
        if ch == '\\': out.append(r'\textbackslash{}')
        elif ch in '{}#%&_': out.append('\\' + ch)
        elif ch == '^': out.append(r'\^{}')
        elif ch == '~': out.append(r'\~{}')
        elif ch == '<': out.append(r'\textless{}')
        elif ch == '>': out.append(r'\textgreater{}')
        elif ch in UNI: out.append(UNI[ch])
        elif ord(ch) > 127: raise ValueError('non-ASCII character %r in text: %r' % (ch, t))
        else: out.append(ch)
    return ''.join(out)
def fmt_text(t):
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t)
    t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\\emph{\1}', t)
    return t
def inline(s):
    # split into math $..$, code `..`, links [..](..), and text
    res, i = [], 0
    pat = re.compile(r'(\$[^$]+?\$)|(`[^`]+?`)|(\[([^\]]+)\]\(([^)]+)\))')
    for m in pat.finditer(s):
        res.append(fmt_text(s[i:m.start()]))
        if m.group(1):
            math = m.group(1)
            for k, v in UNI.items():
                if k in math and v.startswith('$'): math = math.replace(k, v.strip('$'))
            res.append(math)
        elif m.group(2):
            code = m.group(2)[1:-1]
            res.append(r'\texttt{' + esc(code) + '}')
        else:
            res.append(r'\href{' + m.group(5).replace('%', r'\%').replace('#', r'\#') + '}{' + fmt_text(m.group(4)) + '}')
        i = m.end()
    res.append(fmt_text(s[i:]))
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
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}\setlength{\emergencystretch}{3em}\sloppy
\begin{document}
"""
def convert(md):
    lines = md.split('\n'); out = [PRE]; i = 0; n = len(lines)
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
            out.append(r'\[' + '\n' + '\n'.join(buf) + '\n' + r'\]'); i += 1; continue
        if l.strip().startswith('$$') and l.strip().endswith('$$') and len(l.strip()) > 4:
            flush_list(liststack); out.append(r'\[' + l.strip()[2:-2] + r'\]'); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            flush_list(liststack); lev = len(m.group(1)); txt = inline(m.group(2))
            if lev == 1: out.append(r'{\raggedright\LARGE\bfseries ' + txt + r'\par}\medskip')
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
            colw = r'p{\dimexpr %.4f\linewidth-2\tabcolsep\relax}' % w
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
        flush_list(liststack); buf = [l.strip()]; i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(('#', '|', '>', '```', '$$')) and not re.match(r'^\s*([-*]|\d+\.)\s+', lines[i]) and lines[i].strip() != '---':
            buf.append(lines[i].strip()); i += 1
        out.append(inline(' '.join(buf)) + '\n')
    flush_list(liststack); out.append(r'\end{document}'); return '\n'.join(out)
if __name__ == '__main__':
    src = open(sys.argv[1], encoding='utf-8').read()
    open(sys.argv[2], 'w', encoding='ascii').write(convert(src))
