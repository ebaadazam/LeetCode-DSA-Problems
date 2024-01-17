'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
'''

# create a node class with data and next
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# create a function for merging two sorted lists
def merge_sorted_lists(list1, list2):
    dummy = Node()  # a dummy node is created
    tail = dummy  # tail is set to point to this dummy node. The tail pointer will be used to build the merged list.

    # while loop iterates as long as both list1 and list2 are not empty.
    while list1 and list2:

        # the values of the current nodes in list1 and list2 are compared
        if list1.data < list2.data:  # list1.data or list2.data represents the data of a node

            # the smaller value is appended to the merged list through the tail pointer
            tail.next = list1

            # move to next node in the list
            list1 = list1.next  # list1 represents a node
        else:
            tail.next = list2
            list2 = list2.next

        # the tail pointer is then moved to the last appended node.
        tail = tail.next

    # now if either list1 or list2 still has remaining nodes, the remaining nodes are appended to the merged list.
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next

def display(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    print(result)


list1 = Node(1, Node(2, Node(4)))
list2 = Node(1, Node(3, Node(5)))

result = merge_sorted_lists(list1, list2)
display(result)
