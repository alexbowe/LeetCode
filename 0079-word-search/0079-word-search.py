class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H,W = len(board), len(board[0])
        
        board_chars = {board[r][c] for r,c in product(range(H),range(W))}
        word_chars = set(word)
        if word_chars - board_chars: return False
        
        def search(pos, i=0, seen=None):
            r,c = pos
            seen = seen or set()
            if i >= len(word): return True
            if r<0 or c<0 or r>=H or c>=W: return False
            if pos in seen: return False
            if board[r][c] != word[i]: return False
            seen.add(pos)
            result = any([
                search((r-1,c),i+1,seen),
                search((r,c-1),i+1,seen),
                search((r+1,c),i+1,seen),
                search((r,c+1),i+1,seen),
            ])
            seen.remove(pos)
            return result
        return any(search((r,c)) for r,c in product(range(H),range(W)))