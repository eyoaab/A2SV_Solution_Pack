class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        min_val, max_val = float('inf'), float('-inf')
        store = [0] * 100001

        for i in range (len(nums)):
            if nums[i] < min_val: 
                min_val = nums[i]
            if nums[i] > max_val: 
                max_val = nums[i]
            store[nums[i]] += 1
        ans, l, r = 0, min_val, max_val

        while l <= r:
            if store[l] == 0: 
                l += 1
            elif store[r] == 0: 
                r -= 1
            else:
                ans = max(ans, l + r)
                store[l] -= 1
                store[r] -= 1

        return ans