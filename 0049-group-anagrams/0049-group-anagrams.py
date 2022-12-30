class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        key = lambda s: str(sorted(s))
        for s in strs:
            anagrams[key(s)].append(s)
        return list(anagrams.values())