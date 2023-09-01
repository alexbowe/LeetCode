class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        H,W = len(image), len(image[0])
    
        def in_bounds(r,c):
            return 0 <= r < H and 0 <= c < W
        
        def neighbors(r,c):
            yield (r+1, c)
            yield (r, c+1)
            yield (r-1, c)
            yield (r, c-1)

        initial_color = image[sr][sc]
        if initial_color == color: return image

        q = [(sr,sc)]
        while q:
            r,c = q.pop()
            image[r][c] = color
            q.extend([
                (nr,nc) for nr,nc
                in neighbors(r,c)
                if in_bounds(nr,nc)
                and image[nr][nc] == initial_color
            ])
        
        return image