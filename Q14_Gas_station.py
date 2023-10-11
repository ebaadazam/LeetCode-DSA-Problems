'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start
'''

# Logic:
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# difference = [1-3, 2-4, 3-5, 4-1, 5-2] = [-2, -2, -2, 3, 3]
# At first the total will be initialized with 0 and we keep on adding the next number from difference to the total.
# If the total has come around a number that is less than 0 then we are gonna set it to 0 again
# At last we will have the total fuel that can get us back to the starting position

def gas_station(gas, cost):

    # if the total amount of gas is less than the total cost, it’s impossible to complete the journey, no matter where
    # we start. In this case, the function returns -1. If the total gas is greater than or equal to the total cost, then
    # there exists a solution
    if sum(gas) < sum(cost):
        return -1
    else:
        # total keeps track of the remaining gas
        total = 0

        # count keeps track of the starting position of our journey.
        count = 0

        for i in range(len(gas)):
            # For each station, [difference-(gas[i]-cost[i])] calculates the remaining gas by subtracting the cost from
            # the gas obtained at that station and adds it to total. If at any point total becomes less than 0, that
            # means we’ve run out of gas. In this case, we try the next station as our starting position i.e., increment
            # count and reset total to 0.
            total = total + (gas[i]-cost[i])

            # everytime the starting position does not work we reset the total to 0 and start again
            if total < 0:
                total = 0
                count = i + 1
    return count

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(gas_station(gas, cost))