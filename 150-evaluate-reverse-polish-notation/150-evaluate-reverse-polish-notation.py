class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(a/b),
            "*": lambda a,b: a*b,
        }
        
        stack = []
        for x in tokens:
            if x in ops:
                b,a = stack.pop(), stack.pop()
                stack.append(ops[x](a,b))
            else:
                stack.append(int(x))
        
        return stack.pop()