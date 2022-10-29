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

# s = DPSolution()