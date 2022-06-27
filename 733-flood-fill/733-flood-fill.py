class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # check bounds - not needed given constraints
        
        def bounds(image):
            return len(image), len(image[0])
        
        def in_bounds(x):
            row, col = x
            height, width = bounds(image)
            return 0 <= row < height and 0<=col<width
        
        def neighbors(x):
            row, col = x
            height, width = bounds(image)
            if 0<=row-1:     yield (row-1, col)
            if 0<=col-1:     yield (row,   col-1)
            if row+1<height: yield (row+1, col)
            if col+1<width:  yield (row,   col+1)
        
        stack = [(sr,sc)]
        
        original_color = image[sr][sc]
        if original_color == color: return image
        
        while stack:
            row, col = stack.pop()
            
            if image[row][col] != original_color: continue
                
            image[row][col] = color
            stack.extend(n for n in neighbors((row,col)) if in_bounds(n))
            
        return image