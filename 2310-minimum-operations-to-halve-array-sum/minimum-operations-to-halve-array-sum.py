class Solution:
    def halveArray(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        current = sum_
        ans = 0
        heap = []

        for num in nums:
            heappush(heap,-num)

        while  current > sum_ / 2:
            num = -heappop(heap)
            num /= 2
            current -= num
            heappush(heap,-num)
            ans += 1

        return ans    



