class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            s_prime = ""
            for x in s:
                if x == "#": s_prime = s_prime[:-1]
                else: s_prime += x
            return s_prime
        
        return backspace(s) == backspace(t)
        