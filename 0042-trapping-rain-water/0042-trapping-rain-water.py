class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        left_max = 0
        left = [0] * N
        for i in range(N):
            left_max = max(left_max, height[i])
            left[i] = left_max
        
        right_max = 0
        right = [0] * N
        for i in reversed(range(N)):
            right_max = max(right_max, height[i])
            right[i] = right_max
        
        result = 0
        for i in range(N):
            result += min(left[i], right[i]) - height[i]
        
        return result
            