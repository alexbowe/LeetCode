class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return heapq.nsmallest(k, c, key=lambda w: (-c[w],w))