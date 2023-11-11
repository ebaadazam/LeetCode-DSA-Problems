'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1
 < index2 < numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

# One Approach (Prefer this as it is more efficient)
def number(numbers, target):
    i, j = 0, len(numbers)-1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum > target:
            j -= 1
        elif sum < target:
            i += 1
        else:
            return i+1, j+1

numbers = [1, 3, 4, 5, 7, 10, 11]
target = 9
print(number(numbers, target))


# Another Approach (Works fine but time limit exceeded)
def number(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == target:
                return i+1, j+1

arr = [1,2,3,4,4,9,56,90]
target = 8
print(number(arr, target))