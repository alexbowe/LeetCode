class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 1, len(numbers)

        while i < j:
            s = numbers[i-1] + numbers[j-1]
            if s < target: i+=1
            elif s > target: j-=1
            else: return [i,j]
        
        return []