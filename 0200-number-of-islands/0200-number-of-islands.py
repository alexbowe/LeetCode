class UnionFind:
    def __init__(self):
        from collections import defaultdict
        self._parent = dict()
        self._rank = defaultdict(int)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        x,y = sorted([x,y], key=lambda xs:self._rank[xs])
        self._parent[y] = x
        if self._rank[x] == self._rank[y]: self._rank[x] += 1
    
    def find(self, x):
        if x not in self._parent: self._parent[x] = x
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def count(self):
        return sum(1 for x,px in self._parent.items() if x == px)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        
        def neighbors(row, col):
            if row-1 >= 0:     yield (row-1,col)
            if col-1 >= 0:     yield (row,col-1)
            if row+1 < height: yield (row+1, col)
            if col+1 < width:  yield (row, col+1)
        
        uf = UnionFind()
        
        for r in range(height):
            for c in range(width):
                if grid[r][c] == "0": continue
                uf.find((r,c))
                for nr,nc in neighbors(r,c):
                    if grid[nr][nc] == "0": continue
                    uf.union((r,c), (nr,nc))
        
        return uf.count()