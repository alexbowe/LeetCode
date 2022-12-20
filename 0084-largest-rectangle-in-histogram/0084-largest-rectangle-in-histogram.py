class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        for right,x in enumerate(heights+[0]):
            while s and x <= heights[s[-1]]:
                H = heights[s.pop()]
                W = right if not s else right-s[-1]-1
                max_area = max(max_area, W*H)
            s.append(right)
        return max_area
            