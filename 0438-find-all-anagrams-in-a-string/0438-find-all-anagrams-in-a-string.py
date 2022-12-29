class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        W = len(p)
        need = collections.Counter(p)
        missing = W
        result = []
        l = 0
        for r,x in enumerate(s):
            missing -= need[x]>0
            need[x] -= 1
            if r>=W:
                need[s[l]]+=1
                missing+=need[s[l]]>0
                l+=1
            if missing==0:
                result.append(l)
        return result