class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        q = [([], candidates, target)]
        while q:
            partial, options, t = q.pop()
            if t < 0: continue
            if t == 0: result.append(partial)
            for i in range(len(options)):
                q.append((partial + [options[i]], options[i:], t-options[i]))
        return result