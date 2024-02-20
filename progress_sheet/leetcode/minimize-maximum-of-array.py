class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        current_sum = nums[0]
        _sum = nums[0]
        for i in range(1,len(nums)):
            _sum += nums[i]
            if nums[i]>current_sum:
                current_sum = max(current_sum,math.ceil(_sum/(i+1)))
        return current_sum