class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        000
        010
        111
        
          012
        0 000
        1 010
        2 111
        """
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0: continue
                top = mat[row-1][col] if 0<=row-1 else math.inf
                left = mat[row][col-1] if 0<=col-1 else math.inf
                mat[row][col] = min(top+1, left+1)
        
        for row in reversed(range(len(mat))):
            for col in reversed(range(len(mat[0]))):
                if mat[row][col] == 0: continue
                bottom = mat[row+1][col] if row+1<len(mat) else math.inf
                right = mat[row][col+1] if col+1<len(mat[0]) else math.inf
                mat[row][col] = min([mat[row][col], bottom+1, right+1])
        
        return mat