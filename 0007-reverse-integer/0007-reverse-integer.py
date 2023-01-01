class Solution:
    def reverse(self, x: int) -> int:
        if x==0: return 0
        sign, x = x//abs(x), abs(x)
        result = 0
        while x: result = result*10 + x%10; x //= 10
        return sign*result if -2**31 <= sign*result <= 2**31-1 else 0