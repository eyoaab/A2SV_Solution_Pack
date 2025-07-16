class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        for num in nums:
            if num % 2 == 0:
                evens += 1
            else:
                odds += 1
        
        even_dp = 0
        odd_dp = 0
        for num in nums:
            if num % 2 == 0:
                even_dp = max(even_dp, odd_dp + 1)
            else:
                odd_dp = max(odd_dp, even_dp + 1)
        
        return max(evens, odds, even_dp, odd_dp)