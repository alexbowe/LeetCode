class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        H,W = len(board), len(board[0])

        if len(word) > H*W: return False

        board_count = collections.Counter(sum(board, []))
        word_count = collections.Counter(word)
        if not word_count <= board_count: return False

        if board_count[word[0]] > board_count[word[-1]]: word = word[::-1]

        def find(w, row, col, seen = None):
            if not w: return True
            if row < 0 or row >= H: return False
            if col < 0 or col >= W: return False
            if board[row][col] != w[0]: return False
            
            seen = seen or set()
            if (row,col) in seen: return False
            
            seen.add((row,col))
            result = any([
                find(w[1:], row-1,   col, seen),
                find(w[1:], row+1,   col, seen),
                find(w[1:],   row, col-1, seen),
                find(w[1:],   row, col+1, seen),
            ])
            seen.remove((row,col))
            return result
        return any(find(word,r,c) for r,c in product(range(H),range(W)))
