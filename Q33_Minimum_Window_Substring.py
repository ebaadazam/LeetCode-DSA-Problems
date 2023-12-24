'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

def window(s, t):
    if t == "":
        return ""
    countT, countS = {}, {}
    # Hashmap for string 't'; Full
    for i in t:
        countT[i] = t.count(i)
    # countT will look like {'A': 1, 'B': 1, 'C': 1}

    have, need = 0, len(countT)
    resPos = [-1, -1]
    resLen = float("infinity")
    l = 0

    for r in range(len(s)):
        # Hashmap for string 's'; Not full
        c = s[r]
        countS[c] = 1 + countS.get(c, 0)
        # At last the countS will look like {'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 1, 'N': 1}

        if c in countT and countS[c] == countT[c]:
            have += 1

        while have == need:
            # Update our result
            if (r + 1 - l) < resLen:
                resPos = [l, r]
                resLen = (r + 1 - l)

            # Pop from the left of countS
            countS[s[l]] -= 1
            if s[l] in countT and countS[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = resPos

    return s[l : r+1] if resLen != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(window(s, t))