class DPSolution:
    def __init__(self):
        print("This class contains a collection of solutions to various dp problems from leetcode.")
    def climbStairs(self, n:int) -> int:
        """
        EASY
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        (similar to integer partitions but with 'repeats' being counted)

        e.g. input: n =3
        output: 3
        1 + 1 + 1
        1 + 2
        2 + 1
        """
        if n == 1:
            return 1
        psbs = [0] * n
        psbs[0], psbs[1] = 1, 2
        for i in range(2, n):
            with1 = psbs[i - 1]
            with2 = psbs[(i - 1) - 1]
            together = with1 + with2
            psbs[i] = together
        return psbs[n - 1]

    def minCostClimbingStairs(self, cost: [int]) -> int:
        """
        EASY
        You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
        You can either start from the step with index 0, or the step with index 1.
        Return the minimum cost to reach the top of the floor.

        e.g. cost = [10,15,20]
        output = 15
        - pay 15 and climb 2 steps to reach the top
        """
        length = len(cost)

        if length == 1:
            return cost[0]

        # array dp where dp[i] is min cost to climb to the top starting from the ith staircase
        dp = [0] * (length + 1)
        dp[length] = 0  # the cost from the top is 0
        dp[length - 1] = cost[-1]
        # bottom-up solution needed:
        for i in range(length - 2, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

        print(dp)
        return min(dp[0], dp[1])

    # recursive + memo - top down
    memo = []
    def helper(self, nums, i):
        if i >= len(nums):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]
        res = max(nums[i] + self.helper(nums, i + 2), self.helper(nums, i + 1))
        self.memo[i] = res
        return self.memo[i]

    def robWithMemo(self, nums):
        self.memo = [-1] * len(nums)
        return self.helper(nums, 0)

    # iterative + N variables - bottom up (the better solution)
    def rob(self, nums: [int]) -> int:
        '''
        MEDIUM
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

        e.g. input: nums[2,3,2]
        output: 4
        '''
        if len(nums) == 0:
            return 0
        # order: prev2, prev1, nums[i]
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)  # prev1 will become nums[i] when i moves on
            prev2 = temp
        return prev1

    def rob2(self, nums: [int]) -> int:
        '''
        MEDIUM
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

        e.g. input: nums = [2,3,2]
        output: 3
        You cannot rob house 1 and then house 3

        hint: as the first and last house are adjacent the problem can be split into two:
        - rob the 1st house and then see what you can rob excluding the last house
        - rob the 2nd house and then see what you can rob including the last house
        now these sub-problems are just rob1 so have already been solved
        '''
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        prev1 = 0
        prev2 = 0

        house1 = 0

        # this finds the greatest value when robbing house 1
        for i in range(len(nums) - 1):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp

        house1 = prev1
        prev1, prev2 = 0, 0

        # this finds the greatest value when robbing house 2
        for i in range(1, len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp

        return max(prev1, house1)

# s = DPSolution()