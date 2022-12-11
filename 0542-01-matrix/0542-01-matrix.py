class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H,W = len(mat), len(mat[0])
        
        for r,c in product(range(H), range(W)):
            if mat[r][c] == 0: continue
            up = mat[r-1][c] if r-1>=0 else float("inf")
            left = mat[r][c-1] if c-1>=0 else float("inf")
            mat[r][c] = min(up+1, left+1)
        
        for r in reversed(range(H)):
            for c in reversed(range(W)):
                if mat[r][c] == 0: continue
                down = mat[r+1][c] if r+1<H else float("inf")
                right = mat[r][c+1] if c+1<W else float("inf")
                mat[r][c] = min(mat[r][c], down+1, right+1)
        
        return mat