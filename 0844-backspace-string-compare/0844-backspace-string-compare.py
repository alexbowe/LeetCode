class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def apply(s):
            result = []
            for x in s:
                if x == "#":
                    if result: result.pop(); continue
                else: result.append(x)
            return "".join(result)
        
        return apply(s) == apply(t)