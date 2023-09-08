class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H,W = len(mat), len(mat[0])

        for row in range(H):
            for col in range(W):
                if mat[row][col] == 0: continue
                up = mat[row-1][col] if row-1>=0 else float("inf")
                left = mat[row][col-1] if col-1>=0 else float("inf")
                mat[row][col] = min(up, left) + 1
        
        for row in reversed(range(H)):
            for col in reversed(range(W)):
                if mat[row][col] == 0: continue
                down = mat[row+1][col] if row+1<H else float("inf")
                right = mat[row][col+1] if col+1<W else float("inf")
                mat[row][col] = min(down+1, right+1, mat[row][col])

        return mat