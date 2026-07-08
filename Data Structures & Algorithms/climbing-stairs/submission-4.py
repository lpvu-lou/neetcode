class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming (Top-Down)
        memo = {}
        def helper(k):
            if k <= 2:
                return k
            if k not in memo:
                memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]
        return helper(n)