class UnionFind:
    def __init__(self):
        self._parent = dict()
        self._rank = collections.defaultdict(int)
        self._count = 0

    def __contains__(self, x):
        return x in self._parent
    
    def find(self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._count += 1
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        x,y = sorted([x,y], key=self._rank.__getitem__)
        self._parent[x] = y
        self._rank[y] += self._rank[x] == self._rank[y]
        self._count -= 1
    
    def count(self):
        return self._count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()

        def neighbors(r,c):
            yield r-1,c
            yield r+1,c
            yield r,c-1
            yield r,c+1

        ans = []
        for r,c in positions:
            uf.find((r,c))
            for nr,nc in neighbors(r,c):
                if (nr,nc) in uf: uf.union((r,c),(nr,nc))
            ans.append(uf.count())
        return ans
