class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, width = len(mat), len(mat[0])
        
        def neighbors(row,col):
            if 0<=row-1: yield row-1,col
            if 0<=col-1: yield row,col-1
            if row+1<height: yield row+1,col
            if col+1<width: yield row,col+1
        
        level = []
        seen = set()
        
        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0:
                    seen.add((row,col))
                    level.append((row,col))
        
        steps = 0
        while level:
            for row, col in level:
                mat[row][col] = steps

            level = [n for x in level for n in neighbors(*x) if n not in seen]
            seen.update(level)
            steps += 1
            
        return mat