class Solution:
    def climbStairs(self, n: int) -> int:
        # n = number of steps to reach the top of a staircase
        # can climb either 1 or 2 steps at a time
        # distinct ways to reach to the top
        
        # to land on step n, the last move was either a single step (coming from n-1),
        # or a double (coming from step n-2). theres no other way to arrive

        if n <= 2:
            return n
        
        prev, curr = 1, 2
        for _ in range(3, n+1):
            prev, curr = curr, prev + curr

        return curr
        
