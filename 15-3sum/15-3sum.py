class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        nums.sort()
        
        results = []
        for i in range(len(nums)-2):
            x = nums[i]
            if 0<i and x == nums[i-1]: continue
            
            target = -x
            j, k = i+1, len(nums)-1
            while j<k:
                val = nums[j] + nums[k]
                if val <= target:
                    if val == target:
                        results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<len(nums) and nums[j] == nums[j-1]: j+=1
                else:
                    k -= 1
                    while 0<k and nums[k] == nums[k+1]: k-=1
            
        return results
                
            

        