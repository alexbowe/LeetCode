from collections import defaultdict

class UnionFind:
    def __init__(self):
        self._parent = dict()
        self._rank = defaultdict(int)
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        x,y = sorted([x,y], key=lambda x: self._rank[x])
        self._parent[y] = x
        self._rank[x] = self._rank[x] == self._rank[y]
    
    def find(self, x):
        if x not in self._parent: self._parent[x] = x
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def count(self):
        return sum(1 for x,px in self._parent.items() if x==px)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H,W = len(grid), len(grid[0])
        
        def neighbors(r,c):
            if r-1>=0: yield (r-1, c)
            if c-1>=0: yield (r, c-1)
            if  r+1<H: yield (r+1, c)
            if  c+1<W: yield (r, c+1)
        
        uf = UnionFind()
        for r in range(H):
            for c in range(W):
                if grid[r][c] == "0": continue
                uf.find((r,c))
                for nr, nc in neighbors(r,c):
                    if grid[nr][nc] == "0": continue
                    uf.union((r,c), (nr,nc))
        
        return uf.count()