class Solution:
    def isValid(self, s: str) -> bool:
        parens = {a:b for a,b in "() {} []".split()}
        stack = []
        for x in s:
            if x in parens: stack.append(parens[x])
            elif not stack: return False
            elif stack.pop() != x: return False
        return not stack