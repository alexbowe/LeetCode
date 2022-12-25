class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(partial, options, t):
            if t < 0: return
            if t == 0: yield partial
            for i in range(len(options)):
                yield from helper(partial+[options[i]], options[i:], t-options[i])
        return list(helper([], candidates, target))