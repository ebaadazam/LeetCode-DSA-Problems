'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# One Approach (More effective)
def contains_duplicate(nums, k):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict and i - num_dict[num] <= k:
            return True
        num_dict[num] = i
    return False

nums = [1, 2, 3, 1]
k = 3
print(contains_duplicate(nums, k))


# Another Approach
def contains_duplicate(nums, k):
    window = set()
    l = 0
    for i in range(len(nums)):
        if (i - l) > k:
            window.remove(nums[l])
            l += 1
        if nums[i] in window:
            return True
        window.add(nums[i])
    return False

nums = [1, 2]
k = 1
print(contains_duplicate(nums, k))