'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanum
characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

# One Approach
def valid_palindrome(s):
    s = ''.join(i.lower() for i in s if i.isalnum())
    ptr1, ptr2 = 0, -1

    while ptr1 < len(s) // 2:
        if s[ptr1] == s[ptr2]:
            ptr1 += 1
            ptr2 -= 1
        else:
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))


# Another Approach
def valid_palindrome2(s):
    newstr = ""
    for i in s:
        if i.isalnum():
            newstr = newstr + i.lower()
    return newstr == newstr[::-1]
s = "A man, a plan, a canal: Panama"
print(valid_palindrome2(s))


