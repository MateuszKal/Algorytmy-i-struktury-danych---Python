import sys
import find
import export

def display_menu(graph):
    n = ""
    try:
        while(n != "Exit"):
            print("action> ", end="")
            n = input()
            n = n.lower()
            if (n == "help"):
                print("Help\t\t\tShow this message")
                print("Print\t\t\tPrint the graph usin matrix")
                print("Euler\t\t\tFind Eulerian cycle")
                print("Hamilton\t\tFind Hamiltonian cycle")
                print("Tikz\t\t\tSave the graph to a LaTeX file")
                print("Exit\t\t\tExits the program (same as ctrl+D)")
                    
            elif (n == "print"):
                print(graph)

            elif n == 'euler':
                cycle = find.find_euler_cycle(graph)
                if cycle is None:
                    print("No Eulerian cycle exists.")
                else:
                    print("Eulerian cycle:", cycle)

            elif n == 'hamilton':
                cycle = find.find_hamilton_cycle(graph)
                if cycle is None:
                    print("No Hamiltonian cycle exists.")
                else:
                    print("Hamiltonian cycle:", cycle)

            elif n == 'tikz':
                export.tikz(graph, "export.tex")
                
            elif n == 'exit':
                print("Program exited with status: 0")
                break
            else:
                print("Invalid command. Enter 'Help' for a list of commands.")

    except EOFError:
        print("ctrl + D")
        print("Program exited with status: 0")
        sys.exit(1)