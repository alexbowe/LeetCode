class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        W = 9
        SW = 3
        
        def row(r): return [board[r][c] for c in range(W)]
        def col(c): return [board[r][c] for r in range(W)]
        def sqr(r,c): return [board[r*SW+sr][c*SW+sc] for sr,sc in product(range(SW),range(SW))]
        
        def is_valid(xs):
            c = collections.Counter(xs)
            del c["."]
            return not c or max(c.values()) == 1
        
        rows = all(is_valid(row(r)) for r in range(W))
        cols = all(is_valid(col(c)) for c in range(W))
        sqrs = all(is_valid(sqr(r,c)) for r,c in product(range(SW),range(SW)))
        
        return rows and cols and sqrs