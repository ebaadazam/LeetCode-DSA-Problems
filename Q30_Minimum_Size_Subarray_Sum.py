'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a sub-array whose
sum is greater than or equal to target. If there is no such sub-array, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The sub-array [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

def minimum_subarray(nums, target):
    l, r, total = 0, 0, 0
    # initialize res with greater number so that initially it automatically gets overridden with the min value
    res = float("inf")

    while r < len(nums):
        # keep moving 'r' until it becomes greater than target
        total = total + nums[r]
        while total >= target:
            # if it becomes greater then we will count how many numbers are there in the following sub-array
            res = min(r+1-l, res)
            # as it is greater than target and even then we keep on incrementing the 'r' so it will become more large
            # which is pointless. So we keep decrementing the 'l' as well and move it ahead
            total = total - nums[l]
            l += 1
        r += 1
    return 0 if res == float("inf") else res
nums = [2, 3, 1, 2, 4, 3]
target = 7
print(minimum_subarray(nums, target))