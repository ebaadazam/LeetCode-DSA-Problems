'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present
in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


# One Approach (This approach did not work on leetcode because here we are taking extra space and not making changes
# in the same 'nums' array and its TC is O(n))
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#nums = [1, 1, 2]
dict = {}  # dict to store how many times a particular number is repeating
for i in nums:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)  # {0: 2, 1: 3, 2: 2, 3: 2, 4: 1}
unique = []
for i in dict:
    unique.append(i)
print(unique)
print(len(unique))


# Another Approach (This one works but its TC is O(n^2))
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
for i in nums2:
    while nums2.count(i) > 1:
        nums2.remove(i)

print(nums2)


# Best Approach (With less TC i.e, O(n) and not taking any extra/separate space)
def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    ptr1 = 0
    for ptr2 in range(1, len(nums)):
        if nums[ptr2] != nums[ptr1]:
            ptr1 += 1
            nums[ptr1] = nums[ptr2]

    return ptr1 + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums))