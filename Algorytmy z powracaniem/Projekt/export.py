def tikz(graph, file):
        with open(file, 'w') as f:
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n")
            f.write("\\begin{figure}\n")
            f.write("\\centering\n")
            f.write("\\begin{tikzpicture}[auto, node distance=2cm, every loop/.style={},]\n")
            
            num_nodes = len(graph)

            for node in range(num_nodes):
                f.write(f"\\node[draw, circle] ({node+1}) at ({(node+1) * 360/num_nodes}:3cm) {{$ {node+1} $}};\n")
                
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if graph[i][j] == 1:
                        f.write(f"\\path[->] ({i+1}) edge node {{}} ({j+1});\n")
            
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
        print(f"Graph exported to {file}")