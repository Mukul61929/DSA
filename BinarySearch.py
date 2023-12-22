def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Found the target, return its index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target is not in the list

# Input list
sorted_list = [23, 24, 25, 29, 35, 43, 49, 51, 53, 60]
target_value = 43

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target number {target_value} found at index {result}.")
else:
    print(f"Target number {target_value} not found in the list.")
