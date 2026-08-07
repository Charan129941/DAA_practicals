def heapify(arr, n, i):
    largest = i          
    left = 2 * i + 1     
    right = 2 * i + 2    

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_arr = heap_sort(arr)

print("\nSorted Array:", sorted_arr)

print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n log n)")

print("\nSpace Complexity:")
print("O(1) (In-place sorting)")