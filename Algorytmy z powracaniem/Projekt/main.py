#!/usr/bin/env python
import sys
import create_graphs
import menu

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--hamilton", "--non-hamilton"]:
        print("Usage: ./main.py <--hamilton> or <--non-hamilton>")
        sys.exit(1)

    choice = sys.argv[1]

    nodes = int(input("nodes> "))

    if nodes < 10:
        print("The number of nodes must be at least 10.")
        sys.exit(1)

    if choice == "--hamilton": 
        saturation = float(input("saturation> "))

        if saturation not in [30, 70]:
            print("The saturation must be either 30% or 70%.") 
            sys.exit(1)
            
        saturation /= 100
        graph = create_graphs.create_graph(nodes, saturation)
        graph = create_graphs.create_hamiltonian_cycle(graph, nodes)

    elif choice == "--non-hamilton":
        graph = create_graphs.create_non_hamiltonian_graph(nodes)
        create_graphs.isolate_node(graph, 0)
    
    menu.display_menu(graph)


if __name__ == "__main__":
    main()