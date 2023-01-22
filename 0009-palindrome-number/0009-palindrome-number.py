class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        def digits(x):
            while x:
                yield x%10
                x//=10
        
        def reverse(x):
            r = 0
            for d in digits(x):
                r = r*10 + d
            return r
        
        return reverse(x) == x