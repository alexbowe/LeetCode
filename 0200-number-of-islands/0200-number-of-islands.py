class UnionFind:
    def __init__(self):
        self._parent = dict()
        self._rank = collections.defaultdict(int)
        self._count = 0

    def find(self, x):
        if x not in self._parent: self._count += 1
        if x == self._parent.setdefault(x,x): return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x,y = self.find(x), self.find(y)
        if x==y: return
        x,y = sorted([x,y], key=self._rank.__getitem__)
        self._parent[x] = y
        self._rank[y] += self._rank[x] == self._rank[y]
        self._count -= 1
    
    def count(self):
        return self._count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H,W = len(grid), len(grid[0])
        
        def neighbors(r,c):
            if 0<=r-1: yield (r-1,c)
            if 0<=c-1: yield (r,c-1)
        
        uf = UnionFind()
        for r,c in product(range(H),range(W)):
            if grid[r][c] != "1": continue
            uf.find((r,c))
            for nr,nc in neighbors(r,c):
                if grid[nr][nc] != "1": continue
                uf.union((r,c),(nr,nc))
        
        return uf.count()
