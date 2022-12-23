class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return True
        if not board: return False
        
        H,W = len(board), len(board[0])
        board_chars = {board[r][c] for r,c in product(range(H), range(W))}
        word_chars  = set(word)
        if word_chars - board_chars: return False
        
        def search(pos, i=0, visited=None):            
            r,c = pos
            if i == len(word): return True
            if r<0 or c<0 or r>=H or c>=W: return False
            visited = visited or set()
            if (r,c) in visited: return False
            if board[r][c] != word[i]: return False
            visited.add((r,c))
            result = any([
                search((r+1,c),i+1,visited),
                search((r,c+1),i+1,visited),
                search((r-1,c),i+1,visited),
                search((r,c-1),i+1,visited),
            ])
            visited.remove((r,c))
            return result
        
        return any(search((r,c)) for r,c in product(range(H), range(W)))