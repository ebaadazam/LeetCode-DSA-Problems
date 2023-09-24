'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0
'''


# One Approach (Accepted)
def max_profit(prices):
    l, r = 0, 1
    max_var = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_var = max(max_var, profit)
        else:
            l = r
        r += 1

    return max_var

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))


# Another Approach (The Time Limit was exceeded)
def stocks(nums):
    i, j = 0, 1
    max_var = 0
    count = -1
    while i < len(nums)-1:
        if nums[j] > nums[i]:
            count += 1
            max_var = nums[j]
            i, j = i+1, j+1
        else:
            i, j = i+1, j+1
            count += 1

    if max_var:
        k, min_var = 0, nums[0]
        while k < count:
            if nums[k] <= min_var:
                min_var = nums[k]
                k += 1
    else:
        return 0
    return max_var-min_var
nums = [2, 4, 1]
print(stocks(nums))