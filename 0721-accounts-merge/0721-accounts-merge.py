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
        if x == y: return
        x = self.find(x)
        y = self.find(y)
        x,y = sorted([x,y], key=self._rank.__getitem__)
        self._parent[y] = x
        self._rank[x] += self._rank[x] == self._rank[y]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        
        for name,*emails in accounts:
            key = uf.find(emails[0])
            for email in emails:
                uf.union(key, email)
        
        m = collections.defaultdict(set)
        for name,*emails in accounts:
            key = uf.find(emails[0])
            for email in emails:
                m[key].add(email)
        
        result = []
        for name,*emails in accounts:
            key = uf.find(emails[0])
            if key not in m: continue
            ems = sorted(m[key])
            del m[key]
            result.append([name,*ems])
            
        return result