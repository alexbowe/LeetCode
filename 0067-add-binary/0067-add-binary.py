class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(map(int, a))
        b = list(map(int, b))
        
        result = []
        carry = 0
        while (a and b) or carry:
            x = a.pop() if a else 0
            y = b.pop() if b else 0
            val = x+y+carry
            result.append(val%2)
            carry = val//2
        
        result = a + b + result[::-1]
        return "".join(map(str,result))