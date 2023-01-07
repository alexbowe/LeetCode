class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for r,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                l = stack.pop()
                result[l] = r-l
            stack.append(r)
        return result