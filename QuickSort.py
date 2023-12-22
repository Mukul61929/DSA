def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Input list
unsorted_list = []
#print("Enter the Size of the List: ")
n= int(input("Enter the Size of the List: "))
for i in range(n):
    k=int(input(f"Enter the {i+1} element in the list: "))
    unsorted_list.append(k)
sorted_list = quick_sort(unsorted_list)

print("Unsorted list:", unsorted_list)
print("Sorted list:", sorted_list)
