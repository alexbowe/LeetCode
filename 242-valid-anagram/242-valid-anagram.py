class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = dict()
        count_t = dict()
        for x in s:
            count_s[x] = count_s.get(x,0) + 1
        
        for x in t:
            count_t[x] = count_t.get(x,0) + 1
        
        return count_s == count_t