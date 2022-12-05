class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = 0
        level = {0}
        seen = set()
        while level:
            if amount in level: return n
            level = {x+c for c in coins for x in level if x+c <=amount if x+c not in seen}
            seen.update(level)
            n += 1
            
        return -1
        