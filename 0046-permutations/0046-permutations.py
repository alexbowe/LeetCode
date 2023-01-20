class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(partial, opts):
            if not opts: yield partial
            for i in range(len(opts)):
                yield from helper(partial+[opts[i]], opts[:i]+opts[i+1:])
        return list(helper([],nums))