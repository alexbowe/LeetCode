class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(nums, target):
            if target < 0:  return
            if target == 0: yield []
            yield from (
                [nums[i]] + solution
                for i in range(len(nums))
                for solution in helper(nums[i:], target-nums[i])
            )
            
        return list(helper(candidates, target))