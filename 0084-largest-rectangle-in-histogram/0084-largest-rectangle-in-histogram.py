class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        area = 0
        for r,h in enumerate(heights+[0]):
            while s and heights[s[-1]]>=h:
                H = heights[s.pop()]
                W = r if not s else r-s[-1]-1
                area = max(area, H*W)
            s.append(r)
        return area