class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        l,L,R = 0,0,0
        for r,x in enumerate(s,1):
            missing -= need[x]>0
            need[x]-=1
            if missing > 0: continue
            while need[s[l]]<0:
                need[s[l]]+=1
                l+=1
            if R==0 or r-l<R-L: L,R = l,r
        return s[L:R]