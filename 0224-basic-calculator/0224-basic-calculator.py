class Solution:
    def calculate(self, s: str) -> int:
        result, num, sign = 0, 0, 1
        stack = []
        for i,x in enumerate(s):
            if x.isdigit(): num=num*10+int(x)
            if i==len(s)-1 or x in "+-)":
                result += sign*num
                num,sign = 0,1
            
            if   x == "-": sign = -1
            elif x == "+": sign = +1
            elif x == "(":
                stack.extend([result,sign])
                result, sign = 0, 1
            elif x == ")":
                sign, prev_result = stack.pop(), stack.pop()
                result = prev_result + sign*result
                sign = 1
        return result