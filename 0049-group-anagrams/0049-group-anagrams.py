class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for x in strs:
            anagrams["".join(sorted(x))].append(x)
        return [sorted(x) for x in anagrams.values()]