class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = collections.deque([(0,0)])
        seen = set()
        while q:
            n, val = q.popleft()
            if val == amount: return n
            for c in coins:
                if val + c > amount: continue
                if (val+c) in seen: continue
                q.append((n+1, val+c))
                seen.add(val+c)
        return -1