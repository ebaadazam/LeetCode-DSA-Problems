'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

def ransom(ransomNote, magazine):
    hashmap = {}
    for i in magazine:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    count = 0
    for i in ransomNote:
        if i in hashmap and hashmap[i] > 0:
            hashmap[i] -= 1
            count += 1
    if count == len(ransomNote):
        return True
    else:
        return False

    return hashmap

ransomNote = "aa"
magazine = "aab"
print(ransom(ransomNote, magazine))