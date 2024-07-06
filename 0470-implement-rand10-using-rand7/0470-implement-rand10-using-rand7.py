# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int

          0 1 2 3 4 5 6
        0 0 1 2 3 4 5 6
        1 7 8 9 0 1 2 3
        2 4 5 6 7 8 9 0
        3 1 2 3 4 5 6 7
        4 8 9 0 1 2 3 4
        5 5 6 7 8 9|0 1
        6 2 3 4 5 6 7 8

        randN -> randM

        idx = (Nx + y)%M + 1

        """
        N, M = 7, 10
        
        rand = lambda: rand7() - 1
        
        x = rand()
        y = rand()
        if x*N+y >= 40: return self.rand10()
        return (x*N+y)%M + 1