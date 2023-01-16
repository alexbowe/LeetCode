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
            return not c or max(c.values())==1
        
        return all([
            all(is_valid(row(r)) for r in range(W)),
            all(is_valid(col(c)) for c in range(W)),
            all(is_valid(sqr(r,c)) for r,c in product(range(SW),range(SW))),
        ])