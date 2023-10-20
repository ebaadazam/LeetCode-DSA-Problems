'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
'''

def isomorphic(s, t):
    mapST, mapTS = {}, {}
    for i in range(len(s)):
        i, j = s[i], t[i]

        if (i in mapST and mapST[i] != j) or (j in mapTS and mapTS[j] != i):
            return False

        mapST[i] = j
        mapTS[j] = i

    return True

s = 'egge'
t = 'addr'
print(isomorphic(s, t))
