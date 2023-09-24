'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index
'''

# One Approach (Best)
def jump_game(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False

nums = [2, 3, 1, 1, 4]
print(jump_game(nums))



# Another Approach (This one is also working and the time limit has also not exceeded)
def can_jump(nums):
    n = len(nums)
    max_reach = 0  # Initialize the maximum reachable index

    for i in range(n):
        if i > max_reach:
            return False  # If the current index is not reachable, return False

        max_reach = max(max_reach, i + nums[i])  # Update the maximum reachable index

        if max_reach >= n - 1:
            return True  # If we can reach the last index, return True

    return True

nums = [2, 3, 1, 1, 4]
print(can_jump(nums))



# Another Approach (Working fine but time limit exceeded)
def jump_game(nums):
    i = nums[0]  # initialize i with the first element in the nums
    j = 0  # initialize j with the first index position i.e, 0
    n = len(nums)  # len of nums

    while j < n:
        if i > 0 and i < (n-1):
            i, j = i-1, j+1
        else:
            if i < (n-1):
                i = nums[j]
                if i == nums[-1] or i == 0:
                    break

    if i == nums[-1]:
        return True
    else:
        return False

nums = [2, 3, 1, 1, 4]
print(jump_game(nums))