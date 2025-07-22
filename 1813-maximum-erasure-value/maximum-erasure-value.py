class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        store = defaultdict(int)
        ans ,left, current  = 0 ,0 , 0
       
        for num in nums:

            store[num] += 1
            current += num

            while store[num] > 1:
                store[nums[left]] -= 1
                current -= nums[left]
                if  store[nums[left]] == 0:
                    del  store[nums[left]]
                left += 1

            ans = max(ans, current)    
                     
        return ans