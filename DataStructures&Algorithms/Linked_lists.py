class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node

        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
            current_node = self.head
            while current_node:
                if current_node.data == data:
                    return True
                else:
                    current_node = current_node.next
            return False

    def remove_at_beginning(self):
        # The "next" node of the head becomes the new head node
        self.head = self.head.next

    def clear(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count



sushi_preparation = LinkedList()

sushi_preparation.insert_at_end('preparation')
sushi_preparation.insert_at_end('sushi')
sushi_preparation.insert_at_beginning('assemble')
sushi_preparation.insert_at_beginning('clean the fish')

sushi_preparation.search('preparation')

print(sushi_preparation.search('preparation'))
print(sushi_preparation.search('sushi'))
print(sushi_preparation.print_list())
print(sushi_preparation.is_empty())
print(sushi_preparation.size())
print(sushi_preparation.head)
print(sushi_preparation.tail)




