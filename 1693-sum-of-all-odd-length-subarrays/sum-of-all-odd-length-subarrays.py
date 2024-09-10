class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # corner case
        
        res = 0
        freq = 0
        n = len(arr)
        for i in range(n):
            freq = freq - (i + 1) // 2 + (n - i + 1) // 2
            res += freq*arr[i]
        return res