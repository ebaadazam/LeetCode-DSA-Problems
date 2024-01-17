'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos
is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

# Create a Node Class to initialize 'data' and 'next'
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def has_cycle(head):
    slow, fast = head, head  # initialize both pointer at head i.e, 0th position
    while fast is not None and fast.next is not None:  # while fast and fast.next is not null, we will keep moving
        slow = slow.next  # increment by 1
        fast = fast.next.next  # increment by 2

        # if they both becomes equal then its a cycle
        if slow == fast:
            return True
        
    return False

# Create a linked list: 3 -> 2 -> 0 -> -4
head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)

# Create a cycle: -4 -> 2
head.next.next.next.next = head.next

print(has_cycle(head))