class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        total, prefixSum, mod = 0, 0, 10 ** 9 + 7

        for a in arr:
            prefixSum += a
            total += prefixSum % 2
        total += (len(arr) - total) * total
        
        return total % mod