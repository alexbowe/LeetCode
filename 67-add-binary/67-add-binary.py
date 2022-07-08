class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        11
        01
        """
        carry = 0
        bits = []
        
        a = list(a)
        b = list(b)
        
        while a or b or carry>0:
            x = int(a.pop()) if a else 0
            y = int(b.pop()) if b else 0
            total = x + y + carry
            bit = total%2
            carry = total//2
            bits.append(str(bit))
        
        return "".join(bits[::-1])
