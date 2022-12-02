class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [0] * n
        
        for col in range(n):
            table[col] = 1
            
        for row in range(1, m):
            for col in range(1, n):
                table[col] += table[col-1]
        
        return table[-1]