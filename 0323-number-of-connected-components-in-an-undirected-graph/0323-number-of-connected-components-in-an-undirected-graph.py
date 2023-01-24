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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind()
        for v in range(n):
            uf.find(v)
        for u,v in edges:
            uf.union(u,v)
        return uf.count()