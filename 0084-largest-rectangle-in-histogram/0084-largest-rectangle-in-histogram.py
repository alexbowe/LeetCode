class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        s = []
        # Append 0 so we have a rightmost edge
        for i,h in enumerate(heights+[0]):
            while s and h<=heights[s[-1]]:
                # Try each bars height one at a time
                # until we get to a smaller bar
                H = heights[s.pop()]
                # If nothing was smaller than this include all bars
                W = i if not s else i-s[-1]-1
                area = max(area, H*W)
            s.append(i)
        return area