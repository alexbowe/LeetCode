class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return heapq.nsmallest(k, c.keys(), key=lambda x: (-c[x],x))