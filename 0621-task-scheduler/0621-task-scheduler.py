class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        f_max = max(c.values())
        n_max = sum(1 for x in c.values() if x == f_max)
        return max(len(tasks), (f_max-1)*(n+1)+n_max)