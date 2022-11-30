class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        
        # min paths going up/left
        for r in range(height):
            for c in range(width):
                if mat[r][c] == 0: continue
                # If there were no zeros before this point, we are infinitely far away
                up = mat[r-1][c] if r>0 else float("inf")
                left = mat[r][c-1] if c>0 else float("inf")
                mat[r][c] = min(up, left) + 1
        
        # min paths going down/right
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if mat[r][c] == 0: continue
                # If there were no zeros before this point, we are infinitely far away
                down = mat[r+1][c] if r+1<height else float("inf")
                right = mat[r][c+1] if c+1<width else float("inf")
                # Include previous up-left-min in min check
                mat[r][c] = min(min(down, right) + 1, mat[r][c])
        
        return mat