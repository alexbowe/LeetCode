class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        
        iterate from right to left
        carry is (a+b)%2
        
        1
        1
        """
        n = max(len(a), len(b))
        bits = []
        carry = 0
        for i in range(n):
            x = int(a[-i-1]) if i < len(a) else 0
            y = int(b[-i-1]) if i < len(b) else 0
            val = x + y + carry
            carry = val//2
            bits.append(val%2)
        
        if carry > 0: bits.append(carry)
        
        return "".join([str(x) for x in bits][::-1])