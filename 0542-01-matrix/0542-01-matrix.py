class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        N = height*width
        
        for r in range(height):
            for c in range(width):
                if mat[r][c] == 0: continue
                up = mat[r-1][c] if r>0 else N
                left = mat[r][c-1] if c>0 else N
                mat[r][c] = min(up, left) + 1
        
        print(mat)
        
        for r in reversed(range(height)):
            for c in reversed(range(width)):
                if mat[r][c] == 0: continue
                down = mat[r+1][c] if r+1<height else N
                right = mat[r][c+1] if c+1<width else N
                mat[r][c] = min(min(down, right) + 1, mat[r][c])
        
        return mat