class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        i = 0
        while(i < len(nums)):

            if(nums[i] % 3 != 0):
                
                lower = nums[i] - (nums[i] % 3)
                upper = lower + 3

                diff1 = nums[i] - lower
                diff2 = upper - nums[i]

                if(diff1 < diff2):
                    ans += diff1
                else:
                    ans += diff2

            i += 1

        return ans