class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        q = [([], target)]
        while q:
            partial, target = q.pop()
            if target < 0: continue
            if target == 0: result.add(tuple(sorted(partial)))
            for i in range(len(candidates)):
                q.append((partial + [candidates[i]], target-candidates[i]))
        return result