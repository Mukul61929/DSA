def find_duplicates_dict(nums):
    frequency_dict = {}
    duplicates = []

    for num in nums:
        if num in frequency_dict:
            duplicates.append(num)
        else:
            frequency_dict[num] = 1

    return duplicates

# Inserting elements in the array
print("Enter the size of the array: ")
n=int(input())
array = []
for i in range(n):
    print(f"Enter the {i+1} no element in the array: ")
    k=int(input())
    array.append(k)

result = find_duplicates_dict(array)
print("Duplicates:", result)
