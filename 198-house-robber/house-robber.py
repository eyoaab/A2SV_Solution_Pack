class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if  N == 1:
            return nums[0]

        if N == 2:
            return max(nums[0],nums[1])

        store = [0 for i in range(N)]

        store[0] = nums[0]
        store[1] = max(nums[0],nums[1])

        for i in range(2,N):
            current_num = nums[i]
            store[i] = max(store[i-1],store[i - 2] + current_num )

        return store[-1]                   
        