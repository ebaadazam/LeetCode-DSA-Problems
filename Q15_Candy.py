'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

def candy(ratings):
    # arr is the list of the candies and we have filled it with 1 as the minimum candy that each children will get is 1
    arr = [1] * len(ratings)

    # We have run a for loop from the 2nd position because there will be no left neighbours if we start from the first number
    for i in range(1, len(ratings)):

        # if the ratings are higher than previous then increment it from previous rating
        if ratings[i] > ratings[i-1]:
            arr[i] = arr[i-1] + 1

    # We have run a for loop again but now from the 2nd last position because there will be no right neighbours if we
    # start from the last number
    for i in range(len(ratings)-2, -1, -1):

        # if the ratings are higher than successor then put whatever is maximum between the current and successor rating
        # after adding 1 to it.
        if ratings[i] > ratings[i+1]:
            arr[i] = max(arr[i], arr[i+1]+1)

    return sum(arr)

ratings = [5, 4, 3, 5, 6, 2]
print(candy(ratings))