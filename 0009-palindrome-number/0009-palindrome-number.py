class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        def digits(x):
            if not x: yield 0
            while x:
                yield x%10
                x//=10
        
        def reverse(x):
            result = 0
            for d in digits(x):
                result = result*10 + d
            return result
        
        return reverse(x)==x