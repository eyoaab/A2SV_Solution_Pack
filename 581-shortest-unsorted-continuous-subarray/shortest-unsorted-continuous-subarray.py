class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        needed = sorted(nums)
        if needed == nums:
            return 0
        n = len(nums)
        
        left,right = 0,n - 1

        while left < right:
            if nums[left] == needed[left] and  nums[right] == needed[right]:
                left += 1
                right -= 1
            elif nums[left] == needed[left]:
                left += 1

            elif nums[right] == needed[right]:
                right -= 1
            else:
                break    
                    


        return right - left + 1    
