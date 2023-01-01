class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31,2**31-1
        def digits(x):
            if x == 0: yield 0
            while x:
                yield x%10
                x//=10
        if x == 0: return 0
        sign,x = x//abs(x), abs(x)
        result = sign*reduce(lambda a,b: a*10+b, digits(x))
        if MIN <= result <= MAX: return result
        return 0