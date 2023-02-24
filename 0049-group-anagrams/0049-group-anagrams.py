class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = lambda w: str(sorted(w))
        m = collections.defaultdict(list)
        for w in strs: m[key(w)].append(w)
        return [ws for ws in m.values()]