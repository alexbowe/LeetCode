class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Why move the pointer that points to the lowest line?
        - There will be no bigger and further away lines, since we came from the left
        - There *could* however be a bigger and closer line
        - This line could be on either side
        - But if it is on the bigger side, then it would still only be the lower height, now minus 1. It 
        simply cannot get bigger unless you iterate the lower side.
        """
        result = 0
        lo,hi = 0, len(height)-1
        while lo<hi:
            area = min(height[lo],height[hi]) * (hi-lo)
            result = max(result,area)
            if height[lo]<height[hi]: lo+=1
            else:     hi-=1
        return result