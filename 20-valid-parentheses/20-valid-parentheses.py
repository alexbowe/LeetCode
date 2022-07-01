class Solution:
    def isValid(self, s: str) -> bool:
        parens = {x:y for x,y in "{} [] ()".split()}
        stack = []
        for x in s:
            if x in parens.keys():
                stack.append(parens[x])
            else:
                if not stack: return False
                if stack.pop() != x: return False
        return len(stack) == 0
                