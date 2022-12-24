class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit)
        starts,ends,profit = zip(*sorted(zip(startTime,endTime,profit)))
        skip = [bisect.bisect_left(starts,ends[i]) for i in range(N)]
        dp = [0]*(N+1)
        for i in reversed(range(N)):
            dp[i] = max(dp[i+1], profit[i]+dp[skip[i]])
        return dp[0]