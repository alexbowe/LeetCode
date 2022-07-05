class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": lambda x,y: x+y,
               "-": lambda x,y: x-y,
               "*": lambda x,y: x*y,
               "/": lambda x,y: int(x/y)}
        
        def helper(tokens):
            curr = tokens.pop()
            
            if curr not in ops:
                return int(curr)
            
            right = helper(tokens)
            left = helper(tokens)
            
            result = ops[curr](left, right)
            return result
        
        return helper(tokens)