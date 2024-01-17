'''
Reverse a Singly Linked List
A linked list can be reversed either iteratively or recursively
Note: It is not from the Top 150 Interview Questions

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
'''

class Node():
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse(head):
    prev, current = None, head

    while current != None:
        nxt = current.next  # nxt pointer will point to the node after the curr node
        current.next = prev  # Link curr node to prev node
        prev = current  # move the prev node to the next position
        current = nxt  # move the current node to the next position

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

output = reverse(head)

# Print the reversed linked list
while output:
    print(output.data, end=" ")
    output = output.next