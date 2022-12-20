class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height)-1
        max_area = 0
        while lo<hi:
            area = (hi-lo) * min(height[lo], height[hi])
            max_area = max(max_area, area)
            if height[lo] < height[hi]: lo+=1
            else:                       hi-=1
        return max_area