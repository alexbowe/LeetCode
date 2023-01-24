class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        global_max = 0
        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1]
            current_max = max(current_max+profit, profit)
            global_max = max(current_max, global_max)
        return global_max