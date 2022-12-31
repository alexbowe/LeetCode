class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return heapq.nlargest(k, sorted(c.keys()), key=lambda x: c[x])