class Solution:
    def reverse(self, x: int) -> int:
        if not x: return 0
        MIN,MAX = -2**31, 2**31-1
        sign, x = x//abs(x), abs(x)
        result = 0
        while x:
            result = 10*result + x%10
            x//=10
        return sign*result if MIN<=sign*result<=MAX else 0