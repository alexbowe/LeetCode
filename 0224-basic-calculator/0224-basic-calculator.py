class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()

        stack = []
        sign, result, num = +1, 0, 0

        for i,x in enumerate(s):
            # Accumulate digits to find a number
            if x.isdigit(): num = num*10 + int(x)

            # When a number ends, add it to the result
            if i == len(s)-1 or x in "-+)":
                result += sign*num
                sign, num = +1, 0

            # Is the number positive or negative?
            if   x == "+": sign = +1
            elif x == "-": sign = -1

            # If we are starting a new sub-expression
            # We need a new sub-result and sign
            # (num is not needed as we don't allow numbers
            # before parentheses, so it will always be 0)
            elif x == "(":
                stack.append((sign, result))
                sign, result = +1, 0
            elif x == ")":
                prev_sign, prev_result = stack.pop()
                result = prev_result + prev_sign*result
                sign, num = +1, 0

        return result
