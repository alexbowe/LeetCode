# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10_slower(self):
        N,M = 7,10
        rand = lambda: rand7() - 1

        a, b = rand(), rand()
        x = a*N + b
        if x >= 40: return self.rand10()
        return x%M + 1

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

        a, b = rand(), rand()
        x = (a*N+b)
        if x >=40: try again
        return x%M + 1

             E = (40/49)(2) + (1-40/49)(2+E)
        .: 49E = 80 + 18 + 9E
        .: 40E = 98
        .:   E = 98/40 = ~2.45

          0 1 2 3 4 5 6
        0 0 1 2 3 4 5 6
        1 7 8 9 0 1 2 3
        2 4 5 6 7 8 9 0
        3 1 2 3 4 5 6 7
        4 8 9 0 1 2 3 4
        5 5 6 7 8 9 0 1
        6 2 3 4 5 6 7 8
        7 9 0 1 2 3 4 5
        8 6 7 8 9|0 1 2

          0 1 2 3 4 5 6
        0 0 1 2 3 4 5 6
        1 7 8 9 0 1 2 3
        2 4 5 6 7 8 9|0
         
          0 1 2 3 4 5 6
        0 0 1 2 3 4 5 6

        E = (0/7)(1)   + (1-0/7)(40/49)(2)
                       + (1-40/49)(60/63)(3)
                       + (1-40/49)(1-60/63)(20/21)(4)
                       + (1-40/49)(1-60/63)(1-20/21)(4+E)
          = (40/49)(2) + (9/49)(60/63)(3)
                       + (9/49)(3/63)(20/21)(4)
                       + (9/49)(3/63)(1/21)(4+E)
          = 329/150 = ~2.193 < 2.45
        """
        N,M = 7,10
        rand = lambda: rand7() - 1

        def limits(N, M):
            total = N
            while True:
                invalid = total%M
                valid = total - invalid
                yield valid
                total = invalid*N
                
        x = 0
        for limit in limits(N,M):
            x += rand()
            if x < limit: return x%M + 1
            x = (x-limit)*N