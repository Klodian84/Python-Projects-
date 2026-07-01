class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

        if self.head == None:
            self.tail = None

        return current_node.data

    def has_elements(self):
        return self.head != None



class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, data):
        # Add the document to the queue
        self.queue.enqueue(data)

    def print_documents(self):
        # Iterate over the queue while it has elements
        while self.queue.has_elements():
            # Remove the document from the queue
            print("Printing", self.queue.dequeue())

printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()