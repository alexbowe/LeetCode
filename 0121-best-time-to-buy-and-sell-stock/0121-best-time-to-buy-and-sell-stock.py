class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        global_max = 0
        for i in range(1,len(prices)):
            daily_profit = prices[i] - prices[i-1]
            current_max = max(current_max + daily_profit, daily_profit)
            global_max = max(global_max, current_max)
        return global_max