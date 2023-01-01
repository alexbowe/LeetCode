class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False
        
        def digits(x):
            while x: yield x%10; x//=10
        def reverse(x):
            return reduce(lambda a,b: a*10+b, digits(x))
        
        return x == reverse(x)
        