class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        letters = {
            "1": "",     "2": "abc", "3": "def",
            "4": "ghi",  "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz",
            "0": ""
        }
        
        results = [""]
        for d in digits:
            results = [x+c for x in results for c in letters[d]]
        
        return results