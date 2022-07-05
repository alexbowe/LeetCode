class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        max_length = 0
        
        for right,x in enumerate(s):
            if x in chars:
                while x in chars:
                    chars.remove(s[left])
                    left+=1
            
            max_length = max(max_length, right-left+1)
            
            chars.add(x)
        return max_length