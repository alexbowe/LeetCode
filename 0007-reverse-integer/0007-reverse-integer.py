class Solution:
    def reverse(self, x: int) -> int:
        def digits(x):
            while x:
                yield x%10
                x//=10
        
        def reverse(x):
            return reduce(lambda a,b: a*10 + b, digits(x), 0)
        
        sign = 1 if x>=0 else -1
        x = sign*x
        result = sign*reverse(x)
        return result if -2**31 <= result <= 2**31-1 else 0