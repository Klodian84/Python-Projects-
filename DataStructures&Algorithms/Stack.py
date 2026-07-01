class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            new_node.next = self.top
            self.top = new_node
            self.size += 1

    def pop(self):
        # Check if there is a top element
        if self.top is None:
            return None
        else:
            popped_node = self.top
            # Decrement the size of the stack
            self.size -= 1
            # Update the new value for the top node
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data



# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get()
