class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Enqueue operation: Push onto stack1
        self.stack1.append(item)

    def dequeue(self):
        # Dequeue operation:
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            return None

        # Pop from stack2 (front of the queue)
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeue:", queue.dequeue())  # Output: 1

queue.enqueue(4)
print("Is Empty:", queue.is_empty())  # Output: False
print("Size:", queue.size())  # Output: 3
print("Dequeue:", queue.dequeue())  # Output: 2
print("Dequeue:", queue.dequeue())  # Output: 3
print("Dequeue:", queue.dequeue())  # Output: 4
print("Is Empty:", queue.is_empty())  # Output: True
