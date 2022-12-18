class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(partial, options):
            if not options: yield partial
            for i in range(len(options)):
                yield from helper(partial + [options[i]], options[:i] + options[i+1:])
        return list(helper([], nums))