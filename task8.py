class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

def reverse_string(input_str):
    stack = Stack()

    for char in input_str:
        stack.push(char)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Creating the String 
original_str = str(input("Enter the String you want to reverse: "))
reversed_str = reverse_string(original_str)

print("Original String:", original_str)
print("Reversed String:", reversed_str)
