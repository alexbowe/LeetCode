class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        left = []
        for x in height:
            max_left = max(max_left, x)
            left.append(max_left)
        
        max_right = 0
        right = []
        for x in reversed(height):
            max_right = max(max_right, x)
            right.append(max_right)
        right = right[::-1]
        
        total = 0
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]
        
        return total
        