'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

pattern = "abba"
s = "dog cat tuss dog"

def word_pattern(pattern, s):
    str = s.split()
    map1, map2 = {}, {}

    for i in range(len(pattern)):
        s1, s2 = pattern[i], str[i]

        if ((s1 in map1 and map1[s1] != s2) or
                (s2 in map2 and map2[s2] != s1)):
            return False

        #Here the pattern should be the full match, neither less nor more
        if len(pattern) > len(str) or len(pattern) < len(str):
            return False

        map1[s1] = s2
        map2[s2] = s1
    return True

pattern = "abba"
s = "dog cat milk dog"
print(word_pattern(pattern, s))