class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H,W = len(mat), len(mat[0])

        for r,c in product(range(1,H),range(1,W)):
            if mat[r][c] == 0: continue
            mat[r][c] = min(mat[r][c-1]+1, mat[r-1][c]+1)
        
        for r,c in product(range(H-2,-1,-1),range(W-2,-1,-1)):
            if mat[r][c] == 0: continue
            mat[r][c] = min(mat[r][c+1]+1, mat[r+1][c]+1)
        
        print("\n".join("".join(row) for row in mat))
        return mat