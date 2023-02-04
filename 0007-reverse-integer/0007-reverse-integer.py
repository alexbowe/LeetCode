class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        MIN, MAX = -2**31, 2**31-1
        sign, x = x//abs(x), abs(x)
        r = 0
        while x:
            r = r*10 + x%10
            x//=10
        r *= sign
        return r if MIN <= r <= MAX else 0