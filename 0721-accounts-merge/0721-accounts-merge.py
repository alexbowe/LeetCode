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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for name, *emails in accounts:
            uf.find(emails[0])
            for email in emails[1:]:
                uf.union(emails[0], email)
        
        mapping = collections.defaultdict(set)
        for name, *emails in accounts:
            key = uf.find(emails[0])
            mapping[key].update(emails)
        
        result = []
        for name, *emails in accounts:
            key = uf.find(emails[0])
            if key not in mapping: continue
            result.append([name, *sorted(mapping[key])])
            del mapping[key]
        
        return result