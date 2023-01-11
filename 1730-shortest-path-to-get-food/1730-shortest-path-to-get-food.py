class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        H,W = len(grid), len(grid[0])
        
        def neighbors(r,c):
            if r-1>=0: yield (r-1,c)
            if c-1>=0: yield (r,c-1)
            if r+1<H:  yield (r+1,c)
            if c+1<W:  yield (r,c+1)
        
        START = "*"
        FOOD  = "#"
        FREE  = "O"
        OBSTACLE = "X"
        
        level = [(r,c) for r,c in product(range(H),range(W)) if grid[r][c]==START]
        seen = set(level)
        
        count = 0
        while level:
            next_level = []
            for r,c in level:
                if grid[r][c] == FOOD: return count
                for nr,nc in neighbors(r,c):
                    if grid[nr][nc] == OBSTACLE: continue
                    if (nr,nc) in seen: continue
                    seen.add((nr,nc))
                    next_level.append((nr,nc))
            level = next_level
            count+=1
            
        return -1