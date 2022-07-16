class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        d = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        level = [""]
        for x in digits:
            new_level = []
            for y in d[x]:
                for s in level:
                    new_level.append(s+y)
            level = new_level
        return level