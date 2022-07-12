class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        letters = {
            "0":" ",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        results = [""]
        
        for x in digits:
            results = [z+l for z in results for l in letters[x]]
        
        return results