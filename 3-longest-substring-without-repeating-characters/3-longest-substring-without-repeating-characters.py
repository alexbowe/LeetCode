class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import Counter
        c = Counter()
        
        length = 0
        max_length = 0
        start = 0
        for end in range(len(s)):
            x = s[end]
            
            while c[x] > 0:
                c[s[start]] -= 1
                start += 1
                length -= 1
            
            if c[x] == 0:
                c[x] += 1
                length += 1
                max_length = max(max_length, length)
                
        return max_length