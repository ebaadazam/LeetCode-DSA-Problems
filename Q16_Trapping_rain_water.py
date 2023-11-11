'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''


def trap(heights):

    # initialize two pointers: one at starting and other at the end
    i, j = 0, len(heights)-1

    # max_left keeps track of the max element from left so far and max_right keeps track of the max element from right so far
    max_left, max_right = heights[i], heights[j]

    # 'total' stores the total blocks of water between the black blocks
    total = 0

    while i < j:

        # we will increment whichever variable(max_left or max_right) is minimum
        if max_left < max_right:
            i += 1
            max_left = max(max_left, heights[i])
            total = total + (max_left - heights[i])
        else:
            j -= 1
            max_right = max(max_right, heights[j])
            total = total + (max_right - heights[j])

    return total

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(heights))