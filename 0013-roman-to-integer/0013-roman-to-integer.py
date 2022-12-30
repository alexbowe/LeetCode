class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            # Singulars
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            
            # Subtractions
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        result = 0
        while s:
            symbol = s[:2] if s[:2] in mapping else s[:1]
            result += mapping[symbol]
            s = s[len(symbol):]
        return result