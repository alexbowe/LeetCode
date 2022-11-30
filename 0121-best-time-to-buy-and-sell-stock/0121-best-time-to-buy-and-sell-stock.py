class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Price can go up temporarily - don't want to sell prematurely.
        Likewise, we can weather the storm if we can sell higher later.
        Need to find maximum sub-array of daily profits (and losses).
        """
        current_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            daily_profit = prices[i] - prices[i-1]
            current_profit = max(current_profit+daily_profit, daily_profit)
            max_profit = max(max_profit, current_profit)
        return max_profit