from collections import defaultdict

class UnionFind:
    def __init__(self):        
        self._parent = dict()
        self._rank = defaultdict(int)
        
    def find(self, x):
        if x not in self._parent: self._parent[x] = x
        if x == self._parent[x]: return x
        self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        x,y = sorted([x,y], key=lambda x: self._rank[x])
        self._parent[y] = x
        self._rank[x] += self._rank[x] == self._rank[y]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        
        for name, *emails in accounts:
            uf.find(emails[0])
            for i in range(1, len(emails)):
                uf.union(emails[i-1], emails[i])
        
        directory = defaultdict(lambda: {"name": "", "emails": set()})
        for name, *emails in accounts:
            key = uf.find(emails[0])
            entry = directory[key]
            entry["name"] = name
            entry["emails"].update(emails)
        
        result = []
        for entry in directory.values():
            result.append([entry["name"]] + sorted(entry["emails"]))
        
        return result
        
        
            