class Solution:
    def reverse(self, x: int) -> int:
        def digits(x):
            while x:
                yield x%10
                x//=10
        
        sign = -1 if x <0 else +1
        x = abs(x)
        reverse = 0
        for d in digits(x):
            reverse = reverse*10 + d
        
        return sign*reverse if -2**31 <= sign*reverse <= 2**31-1 else 0