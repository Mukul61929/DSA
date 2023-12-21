class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse_in_groups(self, head, k):
        current = head
        next_node = None
        prev = None
        count = 0

        # Count the number of nodes in the current group
        temp = head
        while temp is not None and count < k:
            temp = temp.next
            count += 1

        # If the group size is less than k, do not reverse
        if count < k:
            return head

        # Reverse the nodes in the current group
        while count > 0 and current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count -= 1

        # Recursively reverse the remaining nodes and link the reversed group
        if next_node is not None:
            head.next = self.reverse_in_groups(next_node, k)

        return prev

    def reverse_linked_list_in_groups(self, k):
        self.head = self.reverse_in_groups(self.head, k)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example 
linked_list = LinkedList()
print("Enter the size of the Linked list: ")
n=int(input())

for i in range(n):
    print(f"Enter the {i+1} no element in the linked list: ")
    k=int(input())
    linked_list.push(k)

print("Original Linked List:")
linked_list.print_list()
print("Enter the group number you want to reverse the linked list: ")
k = int(input())
linked_list.reverse_linked_list_in_groups(k)

print(f"Linked List after reversing in groups of {k}:")
linked_list.print_list()
