def sort_strings(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

#input string value
unsorted_strings = []
n = int(input("Enter the size of the String: "))
for i in range(n):
    k=str(input(f"Enter the {i+1} string value: "))
    unsorted_strings.append(k)
sorted_strings = sort_strings(unsorted_strings)

print("Unsorted list of strings:", unsorted_strings)
print("Sorted list of strings:", sorted_strings)
