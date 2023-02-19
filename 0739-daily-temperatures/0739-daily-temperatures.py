class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = [0] * len(temperatures)
        for r,t in enumerate(temperatures):
            while s and temperatures[s[-1]]<t:
                l = s.pop()
                result[l] = r-l
            s.append(r)
        return result