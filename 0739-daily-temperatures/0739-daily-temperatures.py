class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []
        for r,t in enumerate(temperatures):
            while s and temperatures[s[-1]]<t:
                l = s.pop()
                result[l] = r-l
            s.append(r)
        return result