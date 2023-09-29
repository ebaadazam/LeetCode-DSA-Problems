'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j].
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''

def can_jump(nums):
    count = 0
    l = r = 0

    while r < len(nums)-1:
        far = 0
        for i in range(l, r+1):
            far = max(far, i + nums[i])
        l = r+1
        r = far
        count += 1

    return count

nums = [2, 3, 1, 1, 4]
print(can_jump(nums))