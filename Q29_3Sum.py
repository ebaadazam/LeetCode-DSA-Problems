'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def threeSum(nums):
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        # we do not wanna reuse the same value in the same position twice so i>0 means this is not the first value in
        # the input array and n == nums[i-1] means its the same value as before. If both becomes true then skip the
        # current iteration using 'continue'
        if i > 0 and n == nums[i-1]:
            continue

        # Use two pointers approach for the rest two pointers after the 'n' element
        # Initialize 'l' with the element ahead 'n' and 'r' with the last element
        l, r = i+1, len(nums)-1
        while l < r:
            three_sum = n + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                # If after appending 'l' is as same as the previous element then again move it in order to remove the
                # duplicates
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))