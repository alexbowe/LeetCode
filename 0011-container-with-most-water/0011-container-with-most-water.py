class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height)-1
        area = 0
        while lo < hi:
            area = max(area, min(height[lo],height[hi]) * (hi-lo))
            if height[lo] < height[hi]: lo+=1
            else: hi-=1
        return area