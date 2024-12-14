class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        store = defaultdict(int)

        left = 0

        for right in range(len(nums)):
            store[nums[right]] += 1

            while max(store) - min(store) > 2 and left < right:
                store[nums[left]] -= 1
                if store[nums[left]] == 0:
                    del store[nums[left]]

                left += 1

            # ans += left
            ans += right - left + 1

        return ans             
