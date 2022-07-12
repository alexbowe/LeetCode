class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        
        N = height*width
        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0: continue
                top = mat[row-1][col] if 0<=row-1 else N
                left = mat[row][col-1] if 0<=col-1 else N
                mat[row][col] = min(top, left) + 1
        
        for row in reversed(range(height)):
            for col in reversed(range(width)):
                if mat[row][col] == 0: continue
                bottom = mat[row+1][col] if row+1<height else N
                right = mat[row][col+1] if col+1<width else N
                mat[row][col] = min(mat[row][col], bottom+1, right+1)
        
        return mat