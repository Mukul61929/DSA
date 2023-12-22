def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from the left and right halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements from both halves (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result

#Input list values
unsorted_list = []
n=int(input("Enter the size of the List: "))
for i in range(n):
    k=int(input(f"Enter the {i+1} no element into the List: "))
    unsorted_list.append(k)

sorted_list = merge_sort(unsorted_list)

print("Unsorted list:", unsorted_list)
print("Sorted list:", sorted_list)
