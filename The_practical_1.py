def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



print("Sorting Algorithms")
print("1. Bubble Sort")
print("2. Selection Sort")
print("3. Insertion Sort")
print("4. Merge Sort")
print("5. Quick Sort")

choice = int(input("Enter your choice (1-5): "))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

complexity = {
    1: ("O(n)", "O(n²)", "O(n²)"),
    2: ("O(n²)", "O(n²)", "O(n²)"),
    3: ("O(n)", "O(n²)", "O(n²)"),
    4: ("O(n log n)", "O(n log n)", "O(n log n)"),
    5: ("O(n log n)", "O(n log n)", "O(n²)")
}

if choice == 1:
    sorted_list = bubble_sort(numbers)
    algorithm = "Bubble Sort"

elif choice == 2:
    sorted_list = selection_sort(numbers)
    algorithm = "Selection Sort"

elif choice == 3:
    sorted_list = insertion_sort(numbers)
    algorithm = "Insertion Sort"

elif choice == 4:
    sorted_list = merge_sort(numbers)
    algorithm = "Merge Sort"

elif choice == 5:
    sorted_list = quick_sort(numbers)
    algorithm = "Quick Sort"

else:
    print("Invalid Choice!")
    exit()

print("\nAlgorithm Used:", algorithm)
print("Sorted List:", sorted_list)

print("\nTime Complexity:")
print("Best Case   :", complexity[choice][0])
print("Average Case:", complexity[choice][1])
print("Worst Case  :", complexity[choice][2])