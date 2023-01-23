# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        d1,d2=0,1
        for i in range(n):            
            d1,d2=d2,d1+d2
        return d2