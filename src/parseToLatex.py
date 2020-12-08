def dictToLatexFaces(dictFaces):
    arq = open("saidaFaces.txt", "w")  
    arq.write('\\begin{table}[ht]\n\centering\n' +
                '{\\renewcommand\\arraystretch{1.25}\n\\begin{tabular}{ l l }\n')
    for key in dictFaces:
        arq.write("\t\cline{1-1}\cline{2-2}\n" +
                    "\t\\multicolumn{1}{|c|}{$" + key + "$} &\n" +
                    "\t\multicolumn{1}{c|}{$" + "(" + str(dictFaces[key][0]) + ", " + str(dictFaces[key][1]) + ", " + str(dictFaces[key][2]) + ")" + "$}\n" +
                    "\t\\\\ \n")
    arq.write("\hline\n\end{tabular} }\n\caption{Vértices}\n\end{table}")


def dictToLatex(dictVertices):
    arq = open("saidaVertices.txt", "w")  
    arq.write('\\begin{table}[ht]\n\centering\n' +
                '{\\renewcommand\\arraystretch{1.25}\n\\begin{tabular}{ l l }\n')
    for key in dictVertices:
        arq.write("\t\cline{1-1}\cline{2-2}\n" +
                    "\t\\multicolumn{1}{|c|}{$" + key + "$} &\n" +
                    "\t\multicolumn{1}{c|}{$" + str(dictVertices[key]) + "$}\n" +
                    "\t\\\\ \n")
    arq.write("\hline\n\end{tabular} }\n\caption{Vértices}\n\end{table}")

dictVertices = {'v0': (0, 0), 'v1': (6, 4), 'v2': (0, 6), 'v3': (4, 4), 'v4': (6, 0), 'v5': (12, 4), 'v6': (4, 0), 'v7': (4, 6), 'v8': (6, 6), 'v9': (6, 12), 'v10': (0, 4), 'v11': (12, 0), 'v12': (12, 6)}

dictFaces = {'F0': ('v12', 'v9', 'v8'), 'F1': ('v8', 'v9', 'v12'), 'F2': ('v8', 'v9', 'v7'), 'F3': ('v7', 'v9', 'v8'), 'F4': ('v5', 'v12', 'v1'), 'F5': ('v1', 'v12', 'v5'), 'F6': ('v7', 'v9', 'v2'), 'F7': ('v2', 'v9', 'v7'), 'F8': ('v5', 'v12', 'v1'), 'F9': ('v1', 'v12', 'v5'), 'F10': ('v12', 'v8', 'v1'), 'F11': ('v1', 'v8', 'v12'), 'F12': ('v1', 'v8', 'v7'), 'F13': ('v7', 
'v8', 'v1'), 'F14': ('v1', 'v7', 'v3'), 'F15': ('v3', 'v7', 'v1'), 'F16': ('v3', 'v7', 'v2'), 'F17': ('v2', 'v7', 'v3'), 'F18': ('v3', 'v2', 'v10'), 'F19': ('v10', 'v2', 'v3'), 'F20': ('v11', 'v5', 'v4'), 'F21': ('v4', 'v5', 'v11'), 'F22': ('v5', 'v1', 'v4'), 'F23': ('v4', 'v1', 'v5'), 'F24': ('v4', 'v1', 'v6'), 'F25': ('v6', 'v1', 'v4'), 'F26': ('v6', 'v1', 'v3'), 'F27': ('v3', 'v1', 'v6'), 'F28': ('v6', 'v3', 'v10'), 'F29': ('v10', 'v3', 'v6'), 'F30': ('v6', 'v10', 'v0'), 'F31': ('v0', 'v10', 'v6')}



dictToLatex(dictVertices)
dictToLatexFaces(dictFaces)