class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        replacements = [
            ("IV", "iiii"),
            ("IX", "Viiii"),
            ("XL", "xxxx"),
            ("XC", "Lxxxx"),
            ("CD", "cccc"),
            ("CM", "Dcccc"),
            ("i", "I"),
            ("x", "X"),
            ("c", "C"),
        ]
        
        for a,b in replacements:
            s = s.replace(a,b)
        
        result = 0
        for x in s:
            result += m[x]
        
        return result
        