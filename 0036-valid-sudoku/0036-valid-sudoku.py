class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        W,SW = 9,3
        def row(i): return [board[i][c] for c in range(W)]
        def col(i): return [board[r][i] for r in range(W)]
        def sqr(r,c): return [board[r*SW+sr][c*SW+sc] for sr,sc in product(range(SW),range(SW))]
        
        def is_valid(xs):
            c = collections.Counter(xs)
            del c["."]
            return not c or max(c.values())==1
        
        return all([
            all(is_valid(row(i)) for i in range(W)),
            all(is_valid(col(i)) for i in range(W)),
            all(is_valid(sqr(r,c)) for r,c in product(range(SW),range(SW)))
        ])
                
        