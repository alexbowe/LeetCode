class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def apply_backspace(s):
            result = []
            for x in s:
                if x == "#": result.pop() if result else None
                else: result.append(x)
            return "".join(result)
        return apply_backspace(s) == apply_backspace(t)