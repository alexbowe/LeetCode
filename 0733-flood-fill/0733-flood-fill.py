class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color: return image
        
        height = len(image)
        width = len(image[0])
        
        def neighbors(r,c):
            if r-1>=0:      yield (r-1,c)
            if c-1>=0:      yield (r, c-1)
            if r+1<height: yield (r+1, c)
            if c+1<width:  yield (r, c+1)
        
        q = [(sr,sc)]
        while q:
            r,c = q.pop()
            image[r][c] = color
            q.extend((nr,nc) for nr,nc in neighbors(r,c) if image[nr][nc] == original_color)
        
        return image