class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        
        carry = 0
        bits = []
        while a or b or carry:
            x = int(a.pop()) if a else 0
            y = int(b.pop()) if b else 0
            val = x+y+carry
            bit = val%2
            carry = val//2
            bits.append(str(bit))
        
        return "".join(bits[::-1])