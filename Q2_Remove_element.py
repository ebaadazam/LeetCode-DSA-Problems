'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the
elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The
remaining elements of nums are not important as well as the size of nums.

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores)
'''

# One Approach (Using builtin function remove() with TC O(n*m))
def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

nums = [0, 1, 2, 2, 3, 0, 5, 2]
val = 2
print(removeElement(nums, val))


# Another Approach (Without using builtin function remove() with TC O(n))
def remove_element(nums, value):
    k = 0
    for i in range(len(nums)):
        if nums[i] != value:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(nums)