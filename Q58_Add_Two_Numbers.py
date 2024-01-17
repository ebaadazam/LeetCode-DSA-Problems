'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''



class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        node = Node()  # create a node
        curr = node   # current ptr point at the position we're gonna be inserting a new node
        carry = 0

        # while l1 and l2 is not None and carry is not None, the while loop will run
        while l1 or l2 or carry:

            # v1 is the digit of l1 and v2 is the digit of l2
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0

            # compute new digit
            total = v1 + v2 + carry

            # carry logic
            carry = total // 10
            digit = total % 10

            # now that we have the digit we can finally insert it into list
            curr.next = Node(digit)

            # update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return node.next

def convert_linked_list_to_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result

# Create instances of the Node class for the input linked lists
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(4)))

solution = Solution()
result_linked_list = solution.addTwoNumbers(l1, l2)
result_list = convert_linked_list_to_list(result_linked_list)

print(result_list)
