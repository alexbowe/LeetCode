class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        for x in range(1,n+1):
            result[x] = result[x&(x-1)]+1
        return result