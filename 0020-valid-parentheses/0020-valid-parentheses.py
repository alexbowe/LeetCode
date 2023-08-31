class Solution:
    def isValid(self, s: str) -> bool:
        m = {x:y for x,y in "() {} []".split()}
        stack = []
        for x in s:
            if x in m: stack.append(m[x])
            elif not stack: return False
            elif x != stack.pop(): return False
        return not stack