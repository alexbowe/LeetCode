class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        result = 0
        while s:
            if s[:2] in d:
                result += d[s[:2]]
                s = s[2:]
            else:
                result += d[s[:1]]
                s = s[1:]
        return result
            