class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        chars = set()
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            x = s[i]
            
            while x in chars:
                chars.remove(s[start])
                start += 1
            
            chars.add(x)
            max_len = max(max_len, i-start+1)
                
            
        return max_len
            
            