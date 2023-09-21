'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''


def rotate_element(nums, k):
    count = 1
    while count <= k:
        #nums = [nums[i]] + nums[:-1]

        # we could use the below statement instead of the above one as it is dealing with the same array
        nums.insert(0, nums.pop())

        count += 1
    return nums

nums = [-1, -100, 3, 99]
#arr2 = [1, 2, 3, 4, 5, 6, 7]
k = 2
print(rotate_element(nums, k))