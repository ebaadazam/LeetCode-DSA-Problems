'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string
'''


def reverse_words(s):
    i = 0
    result = ""
    s2 = s.rstrip()
    while i <= len(s2):
        while i < len(s) and s[i] == " ":
            i += 1
        j = i + 1
        while j < len(s) and s[j] != " ":
            j += 1
        string = s[i:j]
        if len(result) == 0:
            result = string
        else:
            result = string + " " + result
        i = j + 1
    return result

s = "  Bob    Loves  Alice   "
print(reverse_words(s))