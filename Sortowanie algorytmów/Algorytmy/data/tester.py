from sorts.alg import insertion_sort, shell_sort, selection_sort, heap_sort, quick_sort_random_pivot, quick_sort_left_pivot


algorithmEnum = {
    1: insertion_sort,
    2: shell_sort,
    3: selection_sort,
    4: heap_sort,
    5: quick_sort_left_pivot,
    6: quick_sort_random_pivot
}

testArray = [0,71,1,4345,12,533,5,223]

def sort_using_algorithm(data, algorithm):

    sorted_data = algorithmEnum[algorithm](data)

    return sorted_data

print(sort_using_algorithm(testArray,2))
