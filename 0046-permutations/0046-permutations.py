class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        q = [([], nums)]
        while q:
            partial, candidates = q.pop()
            if not candidates: permutations.append(partial)
            for i in range(len(candidates)):
                q.append((partial + [candidates[i]], candidates[:i] + candidates[i+1:]))
        return permutations