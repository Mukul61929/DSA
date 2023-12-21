def find_kth_largest_and_smallest(nums, k):
    nums.sort()
    
    kth_smallest = nums[k - 1]
    kth_largest = nums[-k]
    
    return kth_smallest, kth_largest

# Inserting elements in the array
print("Enter the size of the array: ")
n=int(input())
array = []
for i in range(n):
    print(f"Enter the {i+1} no element in the array: ")
    k=int(input())
    array.append(k)
print(f"Enter the Kth value that should be less than equal to {n}: ")
k_value = int(input())
if k_value<=n:
    kth_smallest, kth_largest = find_kth_largest_and_smallest(array, k_value)
    print(f"{k_value}th Smallest: {kth_smallest}")
    print(f"{k_value}th Largest: {kth_largest}")
else:
    print("Please enter the kth element value under array range...")
