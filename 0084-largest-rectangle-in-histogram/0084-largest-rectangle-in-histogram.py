class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        s = []
        for i,h in enumerate(heights+[0]):
            while s and h<=heights[s[-1]]:
                H = heights[s.pop()]
                W = i if not s else i-s[-1]-1
                area = max(area, W*H)
            s.append(i)
        return area