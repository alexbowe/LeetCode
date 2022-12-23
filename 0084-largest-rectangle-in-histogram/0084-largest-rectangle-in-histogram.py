class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i,x in enumerate(heights+[0]):
            while stack and x<=heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i if not stack else i-stack[-1]-1
                area = max(area, H*W)
            stack.append(i)
        return area