class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        lo, hi = 0, len(height)-1
        while lo<hi:
            area = min(height[lo],height[hi]) * (hi-lo)
            result = max(result, area)
            if height[lo] < height[hi]: lo+=1
            else: hi-=1
        return result