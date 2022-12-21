class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        totals = {0}
        seen = set()
        n = 0
        while totals:
            if amount in totals: return n
            totals = {x+c for c in coins for x in totals if x+c <= amount and x+c not in seen}
            seen.update(totals)
            n += 1
        return -1