'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
->Starting with any positive integer, replace the number by the sum of the squares of its digits.
->Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
->Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 02 = 1

Example 2:
Input: n = 2
Output: false
'''


# One Approach (More efficient)
def is_happy_number(n):
    def get_next(n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += (digit * digit)
            n //= 10
        return sum

    hashmap = {}

    if n != 1 and n not in hashmap:
        hashmap[n] = True
        n = get_next(n)

    return n == 1

n = 2
print(is_happy_number(n))


# Another Approach (Works fine but less efficient)
def happy_number(n):
    def happy(n, number_map):
        if n == 1:
            return True
        if n in number_map:
            return False

        number_map.add(n)

        sum = 0
        while n > 0:
            l = n % 10
            sq = l * l
            sum += sq
            n //= 10

        return happy(sum, number_map)

    number_map = set()
    return happy(n, number_map)

n = 19
print(happy_number(n))



