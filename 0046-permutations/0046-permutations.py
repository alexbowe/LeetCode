class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(partial, remaining):
            if not remaining: yield partial
            for i in range(len(remaining)):
                yield from helper(partial + [remaining[i]], remaining[:i] + remaining[i+1:])
        return list(helper([], nums))
            