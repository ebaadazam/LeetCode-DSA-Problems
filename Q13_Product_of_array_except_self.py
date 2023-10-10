'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# One Approach (Accepted, it runs in O(n) time and without using the division operation)
def product(nums):
    arr = [1] * len(nums)  # [1, 1, 1, 1]

    prefix = 1
    for i in range(len(arr)):
        arr[i] = prefix
        prefix = prefix * nums[i]

    postfix = 1
    for i in range(len(arr)-1, -1, -1):
        arr[i] = postfix * arr[i]
        postfix = postfix * nums[i]
    return arr
print(product([1, 2, 3, 4]))


# Another Approach (Accepted but we use division operator here)
def product(nums):
    # we will get to know how many zeros are there in the array
    zero_count = nums.count(0)

    # if the count of zeros are greater than one then the whole array will contain 0
    if zero_count > 1:
        return [0]*len(nums)

    # if there is only one 0 in the array
    elif zero_count == 1:

        # The variable n will be used to store the product of all non-zero numbers in the list.
        var = 1
        for i in nums:
            # if the current number is not zero.
            if i != 0:
                var *= i
        return [var if i == 0 else 0 for i in nums]
    else:
        n, arr = nums[0], []
        for i in nums:
            n *= i
        for i in nums:
            rem = n//i
            arr.append(rem)
        return arr

nums = [2, 0, 4, 6]
print(product(nums))

