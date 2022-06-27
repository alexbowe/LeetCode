class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Requirements
        Examples
        Solve
        Pseudocode
        Code
        Test
        
        """
        original_color = image[sr][sc]
        
        if original_color == color: return image

        frontier = [(sr,sc)]
        
        def bounds(image):
            return len(image), len(image[0])
        
        def neighbors(row,col):
            height, width = bounds(image)
            if 0 <= row - 1:   yield (row-1, col)
            if 0 <= col - 1:   yield (row  , col-1)
            if row+1 < height: yield (row+1, col)
            if col+1 < width:  yield (row  , col+1)

        while frontier:
            row, col = frontier.pop()
            image[row][col] = color
            frontier.extend((nr,nc) for (nr,nc) in neighbors(row,col) if image[nr][nc] == original_color)
        
        return image