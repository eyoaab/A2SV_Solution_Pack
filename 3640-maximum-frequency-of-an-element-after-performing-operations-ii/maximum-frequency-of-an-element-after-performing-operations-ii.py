class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = Counter(nums)                
        presum = defaultdict(int)

        for x in count:              
            presum[x - k] += count[x]
            presum[x + k + 1] -= count[x]

        keys = sorted(presum.keys() | count.keys())   
        ans, total = 0, 0

        for x in keys:
            total += presum[x]                          
            ops = min(total - count[x], numOperations)  
            ans = max(ans, count[x] + ops) 

        return ans

