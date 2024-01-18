class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440
        freqs = list(collections.Counter(tasks).values())
        f_max = max(freqs)
        n_max = freqs.count(f_max)
        return max(len(tasks), (n+1)*(f_max-1)+n_max)
