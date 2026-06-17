#!/usr/bin/env python
import sys
import numpy as np
import random

class Graph:
    def __init__(self):
        self.matrix = []
        self.list = []
        self.table = []

    #EXPORT
    def to_tikz(self):
        if self.matrix:
            self.tikz_matrix("matrix-graph.tex")
        elif self.list:
            self.tikz_list("list-graph.tex")
        elif self.table:
            self.tikz_table("table-graph.tex")
        else:
            print("Graph is empty.")
    
    def tikz_matrix(self, file):
        with open(file, 'w') as f:
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n")
            f.write("\\begin{figure}\n")
            f.write("\\centering\n")
            f.write("\\begin{tikzpicture}[auto, node distance=2cm, every loop/.style={},]\n")
            
            num_nodes = len(self.matrix)

            for node in range(num_nodes):
                f.write(f"\\node[draw, circle] ({node+1}) at ({(node+1) * 360/num_nodes}:3cm) {{$ {node+1} $}};\n")
                
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if self.matrix[i][j] == 1:
                        f.write(f"\\path[->] ({i+1}) edge node {{}} ({j+1});\n")
            
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
        print(f"Graph exported to {file}")
    
    def tikz_list(self, file):
        with open(file, 'w') as f:
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n")
            f.write("\\begin{figure}\n")
            f.write("\\centering\n")
            f.write("\\begin{tikzpicture}[auto, node distance=2cm, every loop/.style={},]\n")
            
            num_nodes = max(max(edge) for edge in self.list)  
            
            for node in range(num_nodes):
                f.write(f"\\node[draw, circle] ({node+1}) at ({(node+1) * 360/num_nodes}:3cm) {{$ {node+1} $}};\n")
                
            for edge in self.list:
                f.write(f"\\path[->] ({edge[0]}) edge node {{}} ({edge[1]});\n")
            
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
        print(f"Graph exported to {file}")
        
    def tikz_table(self,file):
        with open(file, 'w') as f:
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n")
            f.write("\\begin{figure}\n")
            f.write("\\centering\n")
            f.write("\\begin{tikzpicture}[auto, node distance=2cm, every loop/.style={},]\n")
            
            num_nodes = len(self.table)
            for node in range(num_nodes):
                f.write(f"\\node[draw, circle] ({node+1}) at ({(node+1) * 360/num_nodes}:3cm) {{$ {node+1} $}};\n")
            for i in range(num_nodes):
                for j in self.table[i]:
                    f.write(f"\\path[->] ({i+1}) edge node {{}} ({j});\n")
            f.write("\\end{tikzpicture}\n")
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
        print(f"Graph exported to {file}")
    #Kahn i Tarjan

    def kahn(self):
        if self.matrix:
            in_degree = [0]*(len(self.matrix))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if self.matrix[i][j] == 1:
                        in_degree[j] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.matrix)):
                    if self.matrix[u][i] == 1:
                        in_degree[i] -= 1
                        if in_degree[i] == 0:
                            queue.append(i)
                count += 1
            if count != len(self.matrix):
                print("Cycle in graph.")
            else:
                print("Kahn: ", [node + 1 for node in top_order])
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list) 
            in_degree = [0] * num_nodes
            for i in range(len(self.list)):
                in_degree[self.list[i][1]-1] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.list)):
                    if self.list[i][0]-1 == u:
                        in_degree[self.list[i][1]-1] -= 1
                        if in_degree[self.list[i][1]-1] == 0:
                            queue.append(self.list[i][1]-1)
                count += 1
            if count != num_nodes:
                print("Cycle in graph.")
            else:
                print("Kahn: ", [node + 1 for node in top_order])
        elif self.table:
            in_degree = [0]*len(self.table)
            for i in range(len(self.table)):
                for j in self.table[i]:
                    in_degree[j-1] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.table)):
                    if i == u:
                        for j in self.table[i]:
                            in_degree[j-1] -= 1
                            if in_degree[j-1] == 0:
                                queue.append(j-1)
                count += 1
            if count != len(self.table):
                print("Cycle in graph.")
            else:
                print("Kahn: ", [node + 1 for node in top_order])
        else:
            print("Graph is empty.")
        
    def tarjan_matrix(self):
        mark = ['unmarked']*len(self.matrix)
        order = []
        def visit(node):
               if mark[node] == 'temp':
                   print("Cycle in graph.")
                   return
               if mark[node] == 'unmarked':
                   mark[node] = 'temp'
                   for i in range(len(self.matrix)):
                       if self.matrix[node][i] == 1:
                           visit(i)
                   mark[node] = 'marked'
                   order.insert(0,node)
        for i in range(len(self.matrix)):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])    
    
    def tarjan_list(self):
        num_nodes = max(max(edge) for edge in self.list)
        mark = ['unmarked']*num_nodes
        order = []
        def visit(node):
            if mark[node] == 'temp':
                print("Cycle in graph.")
                return
            if mark[node] == 'unmarked':
                mark[node] = 'temp'
                for i in self.list:
                    if i[0] == node + 1: 
                        visit(i[1]-1)
                mark[node] = 'marked'
                order.insert(0,node)
        for i in range(num_nodes):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])
        
    def tarjan_table(self):
        mark = ['unmarked']*len(self.table)
        order = []
        def visit(node):
               if mark[node] == 'temp':
                   print("Cycle in graph.")
                   return
               if mark[node] == 'unmarked':
                   mark[node] = 'temp'
                   for i in self.table[node]:
                       visit(i-1)
                   mark[node] = 'marked'
                   order.insert(0,node)
        for i in range(len(self.table)):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])
    
    def tarjan(self):
        if self.matrix:
            self.tarjan_matrix()
        elif self.list:
            self.tarjan_list()
        elif self.table:
            self.tarjan_table()
        else:
            print("Graph is empty.") 

    #Generate

    def generate_dag(self, nodes, saturation, type):
        if type == 'matrix':
                self.matrix = [[0]*nodes for _ in range(nodes)]
                for i in range(nodes):
                    for j in range(i+1, nodes):
                        if random.random() < saturation:
                            self.matrix[i][j] = 1
                return self.matrix
        elif type == 'list':
                for i in range(1, nodes+1):
                    for j in range(i+1, nodes+1):
                        if random.random() < saturation:
                            self.list.append((i, j))
                return self.list
            
        elif type == 'table':
                for i in range(1, nodes+1):
                    row = []
                    for j in range(i+1, nodes+1):
                        if random.random() < saturation:
                            row.append(j)
                    self.table.append(row)
                return self.table

    def user_provided(self, nodes, type):
        if type == 'matrix':
            self.matrix = [[0]*nodes for _ in range(nodes)]
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    for edge in edges:
                        node = int(edge) - 1
                        if node == i:
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= node < nodes:
                            self.matrix[i][node] = 1
                        else:
                            print(f"Node {node+1} does not exist.")
                            break
                    else:  
                        i += 1
            return self.matrix
        elif type == 'list':
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    for edge in edges:
                        if edge == i+1:  
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= edge <= nodes:
                            self.list.append((i+1, edge))  
                        else:
                            print(f"Node {edge} does not exist.")
                            break
                    else:
                        i += 1
            return self.list
        elif type == 'table':
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    row = []
                    for edge in edges:
                        if edge == i+1:  
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= edge <= nodes:
                            row.append(edge)
                        else:
                            print(f"Node {edge} does not exist.")
                            break
                    else:
                        self.table.append(row)
                        i += 1
            return self.table
        else:
            print("Unknown type. Please try again.")
       
    #Find edge

    def find_edge(self):
        try:
            from_node = int(input("from> "))
            to_node = int(input("to> "))
            if from_node < 1 or to_node < 1:
                print("Error: Invalid node number.")
                return
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            return
        if self.matrix:
            if self.matrix[from_node-1][to_node-1] == 1:
                print(f"Edge {from_node} -> {to_node} exists.")
            else:
                print(f"Edge {from_node} -> {to_node} does not exists.")
        elif self.list:
            if (from_node,to_node) in self.list:
                print(f"Edge {from_node} -> {to_node} exists.")
            else:
                print(f"Edge {from_node} -> {to_node} does not exists.")
        elif self.table:
            if to_node in self.table[from_node-1]:
                print(f"Edge {from_node} -> {to_node} exists.")
            else:
                print(f"Edge {from_node} -> {to_node} does not exists.")
        else:
            print("Graph is empty.")

    #PRINT
    def print(self,type):
            if type == 'matrix':
                self.print_matrix()
            elif type == 'list':
                self.print_list()
            elif type == 'table':
                self.print_table()
            else:
                print("Unknown type. Please try again.")

    def print_matrix(self):
        print("    " + "  ".join(str(i) for i in range(1, len(self.matrix)+1)))
        print("--+" + "---"*len(self.matrix))
        for i, row in enumerate(self.matrix, start=1):
           print(f"{i} | {'  '.join(str(cell) for cell in row)}")

    def print_list(self):
        for i, j in self.list:
            print(f"{i} -> {j}")
        
    def print_table(self):
        for i, edges in enumerate(self.table, start=1):  
            print(f"Node {i}:", end=' ')
            for j in edges:
                print(f"{j}", end=' ')
            print()

    #BFS i DFS
        
    def bfs(self):
        if self.matrix:
            for start in range(1, len(self.matrix) + 1):
                visited = [False]*(len(self.matrix)+1)
                order = []
                queue = [start]
                visited[start] = True
                while queue:
                    node = queue.pop(0)
                    order.append(node)
                    for i in range(1, len(self.matrix)+1):
                        if self.matrix[node-1][i-1] == 1 and not visited[i]: 
                            queue.append(i)
                            visited[i] = True
                if all(visited[1:]):
                    return order
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list)
            for start in range(1, num_nodes + 1):
                visited = [False]*(num_nodes+1)
                order = []
                queue = [start]
                visited[start] = True
                while queue:
                    node = queue.pop(0)
                    order.append(node)
                    for edge in self.list:
                        if edge[0] == node and not visited[edge[1]]:
                            queue.append(edge[1])
                            visited[edge[1]] = True
                if all(visited[1:]):
                    return order
        elif self.table:
            for start in range(1, len(self.table) + 1):
                visited = [False]*(len(self.table)+1)
                order = []
                queue = [start]
                visited[start] = True
                while queue:
                    node = queue.pop(0)
                    order.append(node)
                    for i in self.table[node-1]:
                        if not visited[i]:
                            queue.append(i)
                            visited[i] = True
                if all(visited[1:]):
                    return order
        else:
            print("Graph is empty.")
            return None
        print("No valid start node found.")
        return None

    def dfs(self):
        if self.matrix:
            for start in range(1, len(self.matrix) + 1):
                visited = [False]*(len(self.matrix)+1)
                order = []
                stack = [start]
                visited[start] = True
                while stack:
                    node = stack.pop()
                    order.append(node)
                    for i in range(1, len(self.matrix)+1):
                        if self.matrix[node-1][i-1] == 1 and not visited[i]: 
                            stack.append(i)
                            visited[i] = True
                if all(visited[1:]):
                    return order
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list)
            for start in range(1, num_nodes + 1):
                visited = [False]*(num_nodes+1)
                order = []
                stack = [start]
                visited[start] = True
                while stack:
                    node = stack.pop()
                    order.append(node)
                    for edge in self.list:
                        if edge[0] == node and not visited[edge[1]]:
                            stack.append(edge[1])
                            visited[edge[1]] = True
                if all(visited[1:]):
                    return order
        elif self.table:
            for start in range(1, len(self.table) + 1):
                visited = [False]*(len(self.table)+1)
                order = []
                stack = [start]
                visited[start] = True
                while stack:
                    node = stack.pop()
                    order.append(node)
                    for i in self.table[node-1]:
                        if not visited[i]:
                            stack.append(i)
                            visited[i] = True
                if all(visited[1:]):
                    return order
        else:
            print("Graph is empty.")
            return None
        print("No valid start node found.")
        return None

    #MENU

def display_menu(graph, type, g):
    n = ""
    try:
        while(n != "Exit"):
            print("action> ", end="")
            n = input()
            n = n.lower()
            if (n == "help"):
                print("Help\t\t\tShow this message")
                print("Print\t\t\tPrint the graph usin matrix, list or table")
                print("Find\t\t\tFind edges")
                print("BFS\t\t\tBreath-first search")
                print("DFS\t\t\tDepth-first search")
                print("Kahn\t\t\tKahn's Alghorithm")
                print("Tarjan\t\t\tTarjan's Alghorithm")
                print("Tikz\t\t\tSave the graph to a LaTeX file")
                print("Exit\t\t\tExits the program (same as ctrl+D)")
                    
            elif (n == "print"):
                g.print(type)

            elif (n == "find"):
                g.find_edge()

            elif n in ['bfs', 'dfs']:
                if n == 'bfs':
                    print("inline: ", end="")
                    print(g.bfs())
                else:
                    print("inline: ", end="")
                    print(g.dfs())

            elif n == 'kahn':
                g.kahn()
            elif n == 'tarjan':
                g.tarjan()
            elif n == 'tikz':
                g.to_tikz()
            elif n == 'exit':
                print("Program exited with status: 0")
                break
            else:
                print("Invalid command. Enter 'Help' for a list of commands.")

    except EOFError:
        print("ctrl + D")
        print("Program exited with status: 0")
        sys.exit(1)

def main():
    g = Graph()
    if len(sys.argv) < 2 and (sys.argv[1] != "--generate" or sys.argv[1] != "--user-provided"):
        print("Usage: ./graph.py <--generate> or <--user-provided>")
        sys.exit(1)

    choice = sys.argv[1]
    type = input("Type> ")

    if type not in ['matrix', 'list', 'table']:
        print("Invalid type. Please enter 'matrix', 'list', or 'table'.")
        sys.exit()

    nodes = int(input("nodes> "))

    if nodes <= 0:
        print("You provided an incorrect node representation.") 
        sys.exit(1)

    if choice == "--generate": 
        saturation = float(input("saturation> "))

        if saturation < 0 or saturation > 1:
            print("You provided an incorrect saturation representation.") 
            sys.exit(1)

        graph = g.generate_dag(nodes, saturation, type)

    elif choice == "--user-provided":
        graph = g.user_provided_graph_list(nodes, type)

    display_menu(graph, type, g)


if __name__ == "__main__":
    main()