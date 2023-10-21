'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

# One Approach (Accepted with Runtime 7302 ms)
def valid_anagram(s, t):
    mapS, mapT = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        mapS[s[i]] = s.count(s[i])  # Dict of 's' string with the no of occurrences
        mapT[t[i]] = t.count(t[i])  # # Dict of 't' string with the no of occurrences

    flag = True

    for i in mapS:
        if i not in mapT or mapS[i] != mapT[i]:
            flag = False

    return True if flag else False

s = "anagram"
t = "nagaram"
print(valid_anagram(s, t))



# Another Approach (Accepted with Runtime 54 ms, hence more efficient)
def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    map = {}

    for i in s:
        map[i] = map.get(i, 0) + 1

    for char in t:
        if char not in map or map[char] == 0:
            return False
        map[char] -= 1

    return True

s = "anagram"
t = "nagaram"
print(valid_anagram(s, t))