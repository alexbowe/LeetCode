class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f = {
            "*": operator.mul,
            "+": operator.add,
            "-": operator.sub,
            "/": lambda a,b: int(a/b),
        }

        s = []
        for x in tokens:
            if x in f:
                b,a = s.pop(), s.pop()
                s.append(f[x](a,b))
            else: s.append(int(x))
        return s.pop()