import random

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = key
    return arr

## Sedgewick
def shell_sort(arr):
    gaps = [1]
    index = 0
    gap = 1
    while gap < len(arr) // 3:
        index += 1
        gap = (4**index + 3 * 2 **(index-1) + 1)
        gaps.insert(0,gap)

    for gap in gaps:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

## Knuth
# def shell_sort(arr):
#     gaps = [1]
#     gap = 1
#     while gap < len(arr) // 3:
#         gap = 3 * gap + 1
#         gaps.insert(0,gap)

#     for gap in gaps:
#         for i in range(gap, len(arr)):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#     return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def heapArr(arr,n,i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        root = left
    
    if right < n and arr[root] < arr[right]:
        root = right

    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapArr(arr,n,root)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n,-1,-1):
        heapArr(arr,n,i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapArr(arr,i,0)
    return arr

def quick_sort_left_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot=arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x>pivot]
        return quick_sort_left_pivot(less) + [pivot] + quick_sort_left_pivot(greater)
    
def quick_sort_random_pivot(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort_random_pivot(less) + equal + quick_sort_random_pivot(greater)