class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        for right,x in enumerate(heights+[0]):
            # Find the biggest rectangle that ends at right (not including right)
            # To do this, we pop all previous bars that are bigger than right
            # and calculate the rectangle given by that bar up to right (not inclusive).
            # These bars don't get used again - they will always be used in the largest
            # rectangle possible to include them.
            while s and x <= heights[s[-1]]:
                H = heights[s.pop()]
                W = right if not s else right-s[-1]-1
                max_area = max(max_area, W*H)
            s.append(right)
        return max_area
            