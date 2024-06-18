class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0

        for _ in range(k+1):
            new_prices = prices.copy()
            for a,b,cost in flights:
                new_prices[b] = min(new_prices[b], prices[a]+cost)
            prices = new_prices
        
        return prices[dst] if prices[dst]<float("inf") else -1