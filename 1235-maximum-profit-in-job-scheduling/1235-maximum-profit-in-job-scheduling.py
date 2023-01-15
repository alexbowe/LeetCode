class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit)
        s,e,p = zip(*sorted(zip(startTime, endTime, profit)))
        skip = [bisect.bisect_left(s,e[i]) for i in range(N)]
        dp = [0]*(N+1)
        for i in reversed(range(N)):
            dp[i] = max(dp[i+1], p[i]+dp[skip[i]])
        return dp[0]