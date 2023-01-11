class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        W = 9
        SW = 3
        row = lambda r: [board[r][c] for c in range(W)]
        col = lambda c: [board[r][c] for r in range(W)]
        sqr = lambda r,c: [board[r*SW+sr][c*SW+sc] for sr,sc in product(range(SW),range(SW))]
        
        def is_valid(xs):
            c = collections.Counter(xs)
            del c["."]
            return not c or max(c.values()) == 1
        
        valid_rows = all(is_valid(row(r)) for r in range(W))
        valid_cols = all(is_valid(col(c)) for c in range(W))
        valid_sqrs = all(is_valid(sqr(r,c)) for r,c in product(range(SW),range(SW)))
        return valid_rows and valid_cols and valid_sqrs