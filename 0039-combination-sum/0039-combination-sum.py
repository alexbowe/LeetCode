class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(partial, options, target):
            if target < 0: return
            if target == 0: yield partial
            for i in range(len(options)):
                yield from helper(partial+[options[i]], options[i:], target-options[i])
        return list(helper([], candidates, target))