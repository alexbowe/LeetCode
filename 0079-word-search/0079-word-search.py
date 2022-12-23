class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board: return False
        
        H,W = len(board), len(board[0])
        
        board_chars = set(board[r][c] for r,c in product(range(H), range(W)))
        word_chars = set(word)
        if len(word_chars - board_chars) != 0: return False
        
        def neighbors(r,c):
            if r-1>=0: yield (r-1,c)
            if c-1>=0: yield (r,c-1)
            if  r+1<H: yield (r+1,c)
            if  c+1<W: yield (r,c+1)
        
        positions = [(r,c) for r,c in product(range(H), range(W)) if board[r][c] == word[0]]
        
        def dfs(pos, i=0, visited=None):
            visited = visited or set()
            r,c = pos
            if i == len(word): return True
            if any([r<0, c<0, r>=H, c>=W]): return False
            if (r,c) in visited: return False
            if board[r][c] != word[i]: return False
            visited.add((r,c))
            result = any([
                dfs((r+1,c), i+1, visited),
                dfs((r,c+1), i+1, visited),
                dfs((r-1,c), i+1, visited),
                dfs((r,c-1), i+1, visited),
            ])
            visited.remove((r,c))
            return result
        
        return any(dfs(pos) for pos in positions)
        