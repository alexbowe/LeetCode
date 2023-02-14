class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
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
            symbols, s = s[:2], s[2:]
            if symbols in m:
                result += m[symbols]
            else:
                result += m[symbols[0]]
                s = symbols[1] + s
        return result