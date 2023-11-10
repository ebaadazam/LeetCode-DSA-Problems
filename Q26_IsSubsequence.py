'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

# One Approach
def is_subsequence(s, t):
    i, j = 0, 0
    try:
        while i < len(s):
            if s[i] == t[j]:
                i, j = i+1, j+1
            else:
                j += 1
        return True
    except:
        return False

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))


# Another Approach
def is_subsequence2(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(s):
        if s[i] == t[j]:
            i = i+1
        j += 1
    return True if i == len(s) else False

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))