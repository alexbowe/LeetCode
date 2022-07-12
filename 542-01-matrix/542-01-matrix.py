class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H, W = len(mat), len(mat[0])
        N = H*W
        
        for r in range(H):
            for c in range(W):
                if mat[r][c] == 0: continue
                up = mat[r-1][c] if 0<=r-1 else N
                left = mat[r][c-1] if 0<=c-1 else N
                mat[r][c] = min(up+1, left+1)
                
        for r in reversed(range(H)):
            for c in reversed(range(W)):
                if mat[r][c] == 0: continue
                down = mat[r+1][c] if r+1<H else N
                right = mat[r][c+1] if c+1<W else N
                mat[r][c] = min(mat[r][c], down+1, right+1)
        
        return mat