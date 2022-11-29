class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 0:
        1
        
        n = 1:
        1
        
        n = 2:
        2
        
        n = 3:
        3
        
        n = 4:
        5
        1 + 1 + 1 + 1
        1 + 1 + 2
        1 + 2 + 1
        2 + 1 + 1
        2 + 2
        """
        a,b = 1, 1
        for _ in range(n):
            a,b = b,a+b
        return a