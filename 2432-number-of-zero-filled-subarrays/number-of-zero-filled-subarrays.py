class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cur = 0

        for num in nums:
            if num == 0:
                cur += 1
            else:
                ans += ((cur) * (cur + 1  )  ) // 2
                cur = 0
        
        ans += ((cur) * (cur + 1  )  ) // 2



        return ans