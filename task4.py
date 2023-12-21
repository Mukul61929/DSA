def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num

        if complement in seen_numbers:
            pairs.append((num, complement))

        seen_numbers.add(num)

    return pairs

# Inserting elements in the array
print("Enter the Target Sum number: ")
target_sum = int(input())
print("Enter the size of the array: ")
n= int(input())
arr = []
for i in range(n):
    print(f"enter the {i+1} no element in the array: ")
    k=int(input())
    arr.append(k)



result_pairs = find_pairs_with_sum(arr, target_sum)

if result_pairs:
    print(f"Pairs with sum {target_sum}: {result_pairs}")
else:
    print(f"No pairs found with sum {target_sum}")
