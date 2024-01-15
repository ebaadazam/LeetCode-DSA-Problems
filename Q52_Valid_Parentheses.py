'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

# One Approach
def valid_parentheses(s):
    result = []
    for char in s:
        if char in ['(', '{', '[']:
            result.append(char)
        else:
            if char == ')':
                if result and result[-1] == '(':
                    result.pop()
                else:
                    return False

            if char == '}':
                if result and result[-1] == '{':
                    result.pop()
                else:
                    return False

            if char == ']':
                if result and result[-1] == '[':
                    result.pop()
                else:
                    return False
    return True if len(result) == 0 else False

s = '{}{()}'
print(valid_parentheses(s))


# Another Approach
def valid_parentheses2(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in brackets:  # if char is a closing bracket
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
        else:  # if char is an opening brackets
            stack.append(char)
    return True if not stack else False

s = '}{}()'
print(valid_parentheses2(s))