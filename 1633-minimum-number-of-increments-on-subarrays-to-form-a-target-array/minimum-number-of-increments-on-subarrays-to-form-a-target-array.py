class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        prev = 0

        for num in target:
            if num > prev:
                ans += num - prev
            prev = num    

        return ans     