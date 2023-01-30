class UnionFind:
    def __init__(self):
        self._parent = dict()
        self._rank = collections.defaultdict(int)
    
    def find(self, x):
        if x not in self._parent: self._parent[x] = x
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        x,y = sorted([x,y], key=self._rank.__getitem__)
        self._parent[y] = x
        self._rank[x] += self._rank[x] == self._rank[y]
        
    def count(self):
        return sum(x==p for x,p in self._parent.items())

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H,W = len(grid), len(grid[0])
        uf = UnionFind()
        
        def neighbors(r,c):
            if r-1>=0: yield (r-1,c)
            if c-1>=0: yield (r,c-1)
            if r+1<H:  yield (r+1,c)
            if c+1<W:  yield (r,c+1)
        
        for r,c in product(range(H),range(W)):
            if grid[r][c] != "1": continue
            uf.find((r,c))
            for nr,nc in neighbors(r,c):
                if grid[nr][nc] != "1": continue
                uf.union((r,c), (nr,nc))
        
        return uf.count()