Builder`dir = DirectoryName[$InputFileName]; Builder`src = ReadString[FileNameJoin[{Builder`dir, "6planes_src.txt"}]];
Builder`lines = StringSplit[Builder`src, "\n", All];
Builder`blocks = {}; Builder`cur = Null;
Do[Which[
   StringStartsQ[Builder`l, "##TITLE "], (If[Builder`cur =!= Null, AppendTo[Builder`blocks, Builder`cur]]; Builder`cur = {"Title", StringDrop[Builder`l, 8]}),
   StringStartsQ[Builder`l, "##SECTION "], (If[Builder`cur =!= Null, AppendTo[Builder`blocks, Builder`cur]]; Builder`cur = {"Section", StringDrop[Builder`l, 10]}),
   StringStartsQ[Builder`l, "##SUBSECTION "], (If[Builder`cur =!= Null, AppendTo[Builder`blocks, Builder`cur]]; Builder`cur = {"Subsection", StringDrop[Builder`l, 13]}),
   Builder`l === "##TEXT", (If[Builder`cur =!= Null, AppendTo[Builder`blocks, Builder`cur]]; Builder`cur = {"Text", ""}),
   Builder`l === "##CODE", (If[Builder`cur =!= Null, AppendTo[Builder`blocks, Builder`cur]]; Builder`cur = {"Input", ""}),
   True, If[Builder`cur =!= Null, Builder`cur[[2]] = If[Builder`cur[[2]] === "", Builder`l, Builder`cur[[2]] <> "\n" <> Builder`l]]], {Builder`l, Builder`lines}];
AppendTo[Builder`blocks, Builder`cur];
Builder`blocks = {#[[1]], StringTrim[#[[2]]]} & /@ Builder`blocks;
Builder`outFile = FileNameJoin[{Builder`dir, "..", "6planes.nb"}];
Builder`cells = {}; Builder`log = {}; Builder`t0 = AbsoluteTime[]; Builder`k = 0;
Do[If[Builder`b[[1]] =!= "Input", AppendTo[Builder`cells, Cell[Builder`b[[2]], Builder`b[[1]]]],
   Builder`k++;
   AppendTo[Builder`cells, Cell[Builder`b[[2]], "Input", CellLabel -> "In[" <> ToString[Builder`k] <> "]:="]];
   Builder`ed = EvaluationData[ToExpression[Builder`b[[2]], InputForm]];
   Do[AppendTo[Builder`cells, Cell[Builder`m, "Message", "MSG"]]; AppendTo[Builder`log, {Builder`k, Builder`m}], {Builder`m, Builder`ed["MessagesText"]}];
   If[Builder`ed["Result"] =!= Null, AppendTo[Builder`cells, Cell[BoxData[ToBoxes[Builder`ed["Result"], StandardForm]], "Output", CellLabel -> "Out[" <> ToString[Builder`k] <> "]="]]];
   Print["cell ", Builder`k, " done in ", Round[Builder`ed["AbsoluteTiming"], 0.01], " s; messages: ", Length[Builder`ed["MessagesText"]], "; result head: ", Head[Builder`ed["Result"]]]],
  {Builder`b, Builder`blocks}];
Export[Builder`outFile, Notebook[Builder`cells, StyleDefinitions -> "Default.nb"], "NB"];
Print["total time (s): ", Round[AbsoluteTime[] - Builder`t0]];
Print["messages: ", Length[Builder`log]]; Do[Print["MSG in cell ", m[[1]], ": ", StringTake[m[[2]], UpTo[300]]], {m, Builder`log}];
Print["file size: ", FileByteCount[Builder`outFile]];
