class UnionFind:
    def __init__(self):
        self._parent = dict()
        
    def find(self, x):
        if x not in self._parent: self._parent[x] = x
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self._parent[y] = x

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H, W = len(grid), len(grid[0])
        
        def neighbors(pos):
            r,c = pos
            if 0<=r-1: yield r-1,c
            if 0<=c-1: yield r,c-1
            if r+1<H: yield r+1,c
            if c+1<W: yield r,c+1
        
        uf = UnionFind()
        for r in range(H):
            for c in range(W):
                if grid[r][c] == "0": continue
                uf.find((r,c))
                for nr,nc in neighbors((r,c)):
                    if grid[nr][nc] == "0": continue
                    uf.union((r,c),(nr,nc))
        
        count = sum(1 for x in uf._parent.keys() if x == uf._parent[x])
        return count