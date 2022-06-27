class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx = 0
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - prices[min_idx]
            max_profit = max(max_profit, profit)
            if prices[i] < prices[min_idx]: min_idx = i
        
        return max_profit