import sys
from sorts.alg import insertion_sort, shell_sort, selection_sort, heap_sort, quick_sort_random_pivot, quick_sort_left_pivot


algorithmEnum = {
    1: insertion_sort,
    2: shell_sort,
    3: selection_sort,
    4: heap_sort,
    5: quick_sort_left_pivot,
    6: quick_sort_random_pivot
}
def sort_using_algorithm(data, algorithm):
    sys.setrecursionlimit(100000000)
    sorted_data = algorithmEnum[algorithm](data)

    return sorted_data

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data)

if __name__ == "__main__":
    main()
