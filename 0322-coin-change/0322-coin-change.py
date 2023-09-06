class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = 0
        level = {0}
        seen = {0}
        while level:
            if amount in level: return n
            n+=1
            level = {
                v+c for v in level
                for c in coins
                if v+c <= amount
                and v+c not in seen
            }
            seen.update(level)
        return -1
            