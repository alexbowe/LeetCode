class Solution:
    def trap(self, height: List[int]) -> int:
        left  = reduce(lambda xs,x: xs+[max(xs[-1],x)], height, [0])[1:]
        right = reduce(lambda xs,x: xs+[max(xs[-1],x)], height[::-1], [0])[1:][::-1]
        return sum(min(l,r)-h for l,r,h in zip(left,right,height))