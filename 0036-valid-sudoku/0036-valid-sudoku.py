class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        W = 9
        SW = 3
        
        def get_row(r): return board[r]
        def get_col(c): return [board[r][c] for r in range(W)]
        def get_sqr(sr,sc): return [board[sr*SW + r][sc*SW + c] for r,c in product(range(SW),range(SW))]
        
        def is_valid(xs):
            c = collections.Counter(xs)
            del c["."]
            return not c or max(c.values()) == 1
        
        rows = all(is_valid(get_row(r)) for r in range(W))
        cols = all(is_valid(get_col(c)) for c in range(W))
        sqrs = all(is_valid(get_sqr(r,c)) for r,c in product(range(SW),range(SW)))
        return rows and cols and sqrs