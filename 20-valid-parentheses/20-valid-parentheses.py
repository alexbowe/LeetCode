class Solution:
    def isValid(self, s: str) -> bool:
        parens = {x:y for x,y in "{} [] ()".split()}
        
        stack = []
        for x in s:
            if x in parens:
                stack.append(parens[x])
            else:
                if len(stack) == 0: return False
                if stack.pop() != x: return False
        return len(stack) == 0