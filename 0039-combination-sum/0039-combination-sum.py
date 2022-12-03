class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        q = [([], candidates, target)]
        while q:
            partial, candidates, target = q.pop()
            if target < 0: continue
            if target == 0: solutions.append(partial)
            for i in range(len(candidates)):
                q.append((partial+[candidates[i]], candidates[i:], target-candidates[i]))
        return solutions