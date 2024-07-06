class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        prev_op = "+"
        num = 0
        op = {
            "+": lambda x: stack.append(x),
            "-": lambda x: stack.append(-x),
            "*": lambda x: stack.append(stack.pop()*x),
            "/": lambda x: stack.append(int(stack.pop()/x)),
        }
        for x in s+"+":
            if x.isdigit():
                num = 10*num + int(x)
            elif x in "+-*/":
                op[prev_op](num)
                num = 0
                prev_op = x
        return sum(stack)
