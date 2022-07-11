class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Input:
        - array of coin denominations (infinite number of each denomination)
        - amount to add up to
        
        Output:
        - Fewest number of coins
        - -1 if no solution
        
        Fewest number => BFS? Dijkstra?
        Distance is num hops, so BFS should be fine
        Each coin denomination is the edge
        
        Loops wont be a problem because the amount will go over (and no negative coins)
        """
        
        seen = set()
        q = collections.deque([(0, 0)])
        while q:
            num, total = q.popleft()
            if total > amount: continue
            if total == amount: return num
            
            for c in coins:
                if total+c in seen: continue
                seen.add(total+c)
                q.append((num+1,total+c))
            
        return -1