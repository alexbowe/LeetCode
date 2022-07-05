class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        counts = defaultdict(int)
        for x in magazine:
            counts[x]+=1
        
        for x in ransomNote:
            if counts[x] == 0:
                return False
            counts[x]-=1
        
        return True