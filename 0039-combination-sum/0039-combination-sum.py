class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        q = [([], candidates, target)]
        while q:
            partial, options, target = q.pop()
            if target < 0: continue
            if target == 0: result.append(partial)
            for i in range(len(options)):
                q.append((partial + [options[i]], options[i:], target-options[i]))
        return result