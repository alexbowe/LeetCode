class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(profit)
        start, end, profit = zip(*sorted(zip(startTime,endTime,profit)))
        next_available_job = [bisect.bisect_left(start,end[i]) for i in range(N)]

        # If we started working at the last job only, that would be the max
        # profit for that job. With this insight, we can work backwards
        # to find whether or not to do each job.
        # N+1 because the very least profit is obtained by not doing any jobs.
        dp = [0] * (N+1)
        for i in reversed(range(N)):
            # We either skip this job (dp[i+1]) or do it and add its
            # profit to the profit for the next possible job slot.
            dp[i] = max(dp[i+1], profit[i] + dp[next_available_job[i]])
        return dp[0]
