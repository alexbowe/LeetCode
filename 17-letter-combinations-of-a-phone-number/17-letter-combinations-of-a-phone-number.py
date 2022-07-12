class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        letters = {
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
        for d in digits:
            level = [l + x for l in level for x in letters[d]]
        
        return level
        