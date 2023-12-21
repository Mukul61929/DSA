def move_negatives_to_one_side(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            # Swap positive element on the left with negative element on the right
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1

# inserting elements in the array
print("Enter the size of the array: ")
n=int(input())
array = []
for i in range(n):
    print(f"Enter the {i+1} no element in the array: ")
    k=int(input())
    array.append(k)

print("Original Array:", array)

move_negatives_to_one_side(array)
print("Array after moving negatives to one side:", array)
