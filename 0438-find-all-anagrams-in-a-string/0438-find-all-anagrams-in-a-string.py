class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        result = []
        W = len(p)
        need = collections.Counter(p)
        missing = W
        l = 0
        for r,c in enumerate(s):
            missing-=need[c]>0
            need[c]-=1
            if r>=W:
                need[s[l]]+=1
                missing+=need[s[l]]>0
                l+=1
            if missing == 0:
                result.append(l)
        return result