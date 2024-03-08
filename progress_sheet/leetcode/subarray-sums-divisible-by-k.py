from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1 
        current = 0
        answer = 0

        for num in nums:
            current = (current + num) % k  
            answer += prefix_sum[current]
            prefix_sum[current] += 1 

        return answer
