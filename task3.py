class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_alternate_positions(list1, list2):
    if not list1 or not list2:
        return list1 or list2

    current1, current2 = list1, list2

    while current1 and current2:
        temp1, temp2 = current1.next, current2.next

        current1.next = current2
        current2.next = temp1

        current1, current2 = temp1, temp2

    return list1

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example
list1 = Node(1)
list1.next = Node(5)
list1.next.next = Node(7)

list2 = Node(2)
list2.next = Node(6)
list2.next.next = Node(8)

print("List 1:")
print_linked_list(list1)

print("\nList 2:")
print_linked_list(list2)

merged_list = merge_alternate_positions(list1, list2)

print("\nMerged List:")
print_linked_list(merged_list)
