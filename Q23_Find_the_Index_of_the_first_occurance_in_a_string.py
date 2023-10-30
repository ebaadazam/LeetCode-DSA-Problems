'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not a part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1
'''

def first(haystack, needle):
    index = -1
    length = 0
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
            index = i
            length = len(needle)
            break
    return -1 if len(needle) != length else index

haystack = "sadbutsad"
needle = "but"
print(first(haystack, needle))
