class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = [(0,0)]
        seen = set()
        while q:
            n,total = q.pop(0)
            if total == amount: return n
            q.extend((n+1,total+c) for c in coins if total+c<=amount and total+c not in seen)
            seen.update(total+c for c in coins)
        return -1
            