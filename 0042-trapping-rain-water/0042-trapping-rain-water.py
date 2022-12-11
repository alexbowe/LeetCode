class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        max_left = 0
        left = [0] * N
        for i in range(N):
            max_left = max(max_left, height[i])
            left[i] = max_left
        
        max_right = 0
        right = [0] * N
        for i in reversed(range(N)):
            max_right = max(max_right, height[i])
            right[i] = max_right
        
        total = 0
        for i in range(N):
            total += min(left[i], right[i]) - height[i]
        
        return total
        