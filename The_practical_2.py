def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print("Search Algorithms")
print("1. Linear Search")
print("2. Binary Search")

choice = int(input("Enter your choice (1-2): "))

arr = list(map(int, input("Enter elements separated by spaces: ").split()))
key = int(input("Enter the element to search: "))

if choice == 1:
    result = linear_search(arr, key)
    algorithm = "Linear Search"
    best = "O(1)"
    average = "O(n)"
    worst = "O(n)"

elif choice == 2:
    arr.sort()
    print("Sorted Array:", arr)

    result = binary_search(arr, key)
    algorithm = "Binary Search"
    best = "O(1)"
    average = "O(log n)"
    worst = "O(log n)"

else:
    print("Invalid Choice!")
    exit()

print("\nAlgorithm Used:", algorithm)

if result != -1:
    print(f"Element {key} found at index {result}.")
else:
    print(f"Element {key} not found.")

print("\nTime Complexity:")
print("Best Case   :", best)
print("Average Case:", average)
print("Worst Case  :", worst)