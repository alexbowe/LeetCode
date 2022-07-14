class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        H,W = len(image), len(image[0])
        
        original_color = image[sr][sc]
        if color == original_color: return image
        
        def neighbors(row, col):
            if 0<=row-1: yield (row-1, col)
            if 0<=col-1: yield (row, col-1)
            if row+1<H: yield (row+1, col)
            if col+1<W: yield (row, col+1)
        
        stack = [(sr,sc)]
        seen = set()
        while stack:
            row,col = stack.pop()
            if image[row][col] != original_color: continue
            image[row][col] = color
            ns = list(neighbors(row,col))
            stack.extend(n for n in ns if n not in seen)
            seen.update(ns)
        
        return image