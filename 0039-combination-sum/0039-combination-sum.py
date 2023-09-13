class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(partial, opts, rem):
            if rem < 0: return
            if rem == 0: yield partial; return
            for i in range(len(opts)):
                # For combinations, replacement is allowed and order doesn't matter.
                # Using opts[i:] forces the DFS to expand in order of candidates so
                # we do not need a visited set. If the candidates had repeats, we could
                # store solutions as indexes into candidates instead.
                yield from helper(partial + [opts[i]], opts[i:], rem-opts[i])
        return list(helper([], candidates, target))
