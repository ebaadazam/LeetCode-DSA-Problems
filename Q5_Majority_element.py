'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than (n / 2) times. You may assume that the majority element always exists in the array

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


# One Approach (Best One with Time Complexity of O(n))

# This approach is called Moore's Voting Algorithm
def majority_elem(nums):
    majority = nums[0]  # assume the first element as the majority element
    count = 1  # for how many times the majority element has occurred
    i = 1
    while i < len(nums):
        if nums[i] == majority:
            count += 1  # count becomes 0
            i += 1
        else:
            count -= 1
            i += 1
            if count == 0:
                majority = nums[i]
                count = 1
                i += 1
    return majority

nums = [6, 5, 6]
print(majority_elem(nums))


#
# # Another Approach (With this approach, the time limit has been exceeded)
# def majority_element(nums):
#     n = nums[0]
#     while n > 0:
#         if nums.count(n) > (n // 2):
#             return n
#
# nums = [6, 5, 5]
# print(majority_element(nums))
