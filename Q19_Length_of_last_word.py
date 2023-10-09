'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6
'''

# One Approach (Without using any built-in function)
def lenString(string):
    count = 0
    str = string.rstrip()
    i = len(str) - 1
    while i > -1:
        if str[i] != ' ':
            count += 1
            i -= 1
        else:
            break
    return count
print(lenString("   fly me   to   the moon  "))
print(lenString("this is my new normal"))
print(lenString("   fly me   to   the moon"))


# Another Approach (Using split() built-in function)
def lengthStr(string):
    str = string.split(' ')
    return len(str[-1])
print(lengthStr("the quick brown fox jumps over lazydog"))