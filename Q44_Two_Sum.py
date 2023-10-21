'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

# One Approach (Effective Approach with hashmap)
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i

    return None

nums = [3, 2, 3]
target = 6
print(two_sum(nums, target))


# Another Approach (Accepted But with 2511 ms Runtime and without hashmap and Time Complexity O(n**2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return i, j

nums = [2, 5, 5, 11]
target = 10
print(two_sum(nums, target))