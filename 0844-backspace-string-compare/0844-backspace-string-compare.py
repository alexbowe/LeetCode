class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            xs = []
            for c in s:
                if c=="#": xs = xs[:-1]; continue
                xs.append(c)
            return "".join(xs)
        
        return backspace(s) == backspace(t)