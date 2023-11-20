'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

def sequence(nums):
    num_set = set(nums)
    longest = 0
    for i in num_set:
        # If the previous number is not in nums means if it makes the start of the sequence
        if (i-1) not in num_set:
            count = 0

            # If the successor of a number is in the list then increment the count to get the length of sequence until
            # we reach to a number that is no longer in the list
            while (i+count) in num_set:
                count += 1
            longest = max(count, longest)
    return longest

nums = [100, 4, 200, 1, 3, 2]
print(sequence(nums))