'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

def groupAnagrams(strs):
    from collections import defaultdict

    # We used defaultdict to avoid having to initialize an empty array for your keys every single time. DefaultDict will
    # have an empty array or other type of data assigned to a key by default.
    hashmap_anagrams = defaultdict(list)

    # We are creating an empty array named result and will be adding values to it later
    result = []

    for i in strs:
        sorted_keys = tuple(sorted(i))
        #print('sorted_keys = ', sorted_keys)
        hashmap_anagrams[sorted_keys].append(i)
        #print('hashmap_anagrams = ', hashmap_anagrams)

    for value in hashmap_anagrams.values():
        result.append(value)

    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))