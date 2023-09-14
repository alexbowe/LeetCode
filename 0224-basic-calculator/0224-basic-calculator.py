class Solution:
    def calculate(self, s: str) -> int:
        result, sign, num = 0, +1, 0
        stack = []
        for i,x in enumerate(s):
            if x.isdigit(): num = 10*num + int(x)
            if i == len(s)-1 or x in "+-)":
                result += sign*num
                sign, num = +1, 0
            
            if x == "-": sign = -1
            if x == "+": sign = +1
            if x == "(":
                stack.extend([result, sign])
                sign, result = +1, 0
            if x == ")":
                sign, prev_result = stack.pop(), stack.pop()
                result = prev_result + sign*result
                sign = +1
        return result