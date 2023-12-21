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

def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)

    return stack.pop()

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

# Type the string with combinatio of operators
postfix_expression = str(input("Enter the strings with operators: "))
result = evaluate_postfix(postfix_expression)
print("Result of postfix expression:", result)
