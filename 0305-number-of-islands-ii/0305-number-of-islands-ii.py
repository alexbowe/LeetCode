class UnionFind:
    def __init__(self):
        self._rank   = collections.defaultdict(int)
        self._parent = dict()
        self._count  = 0
    
    def find(self, x):
        if x not in self._parent: self._count += 1
        if x == self._parent.setdefault(x, x): return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y: self._count -= 1
        x, y = sorted([x,y], key=self._rank.__getitem__)
        self._parent[y] = x
        self._rank[x] += self._rank[x] == self._rank[y]
    
    def count(self):
        return self._count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def neighbors(r,c):
            if 0<=r-1: yield (r-1,c)
            if 0<=c-1: yield (r,c-1)
            if  r+1<m: yield (r+1,c)
            if  c+1<n: yield (r,c+1)
        
        s = set()
        uf = UnionFind()
        result = []

        for r,c in positions:
            uf.find((r,c))
            for nr,nc in neighbors(r,c):
                if (nr,nc) in s: uf.union((nr,nc),(r,c))
            s.add((r,c))
            result.append(uf.count())
        
        return result