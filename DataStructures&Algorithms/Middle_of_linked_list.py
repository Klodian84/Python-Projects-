class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def middle_of_linked_list(head:Node):
    slow = fast = head # initially both pointer are at the head of the list.
    while fast and fast.next: # while fast and fast.next are still valid.
        fast = fast.next.next # move fast two positions.
        slow = slow.next # move slow one position
    return slow.value

"""
One traversal, no extra space, and it works for both 
odd and even length lists. 
"""