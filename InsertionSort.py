def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage:
unsorted_list = []
n=int(input("Enter the size of the list: "))
for i in range(n):
    k=int(input(f"Enter the {i+1} no element in the list: "))
    unsorted_list.append(k)
insertion_sort(unsorted_list)

print("Unsorted list:", unsorted_list)
