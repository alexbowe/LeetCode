class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY  = 0
        FRESH  = 1
        ROTTEN = 2
        
        H,W = len(grid), len(grid[0])
        
        def neighbors(r,c):
            if r-1>=0: yield (r-1,c)
            if c-1>=0: yield (r,c-1)
            if  r+1<H: yield (r+1,c)
            if  c+1<W: yield (r,c+1)
                
        fresh = {(r,c) for r,c in product(range(H),range(W)) if grid[r][c] == FRESH}
        rotten = {(r,c) for r,c in product(range(H),range(W)) if grid[r][c] == ROTTEN}
        ticks = 0
        while rotten and fresh:
            ticks += 1
            rotten = {(nr,nc) for r,c in rotten for nr,nc in neighbors(r,c) if (nr,nc) in fresh}
            fresh.difference_update(rotten)
        return ticks if not fresh else -1