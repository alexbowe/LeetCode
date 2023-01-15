class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H,W = len(board), len(board[0])
        
        def search(pos, i=0, seen=None):
            r,c = pos
            if i >= len(word): return True
            if r<0 or c<0 or H<=r or W<=c: return False
            if (r,c) in (seen := seen or set()): return False
            if word[i] != board[r][c]: return False
            seen.add((r,c))
            result = any([
                search((r+1,c),i+1,seen),
                search((r-1,c),i+1,seen),
                search((r,c+1),i+1,seen),
                search((r,c-1),i+1,seen),
            ])
            seen.remove((r,c))
            return result
        
        return any(search((r,c)) for r,c in product(range(H),range(W)))