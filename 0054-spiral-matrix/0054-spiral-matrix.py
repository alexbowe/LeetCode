class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + [*self.spiralOrder([*zip(*matrix)][::-1])]
        