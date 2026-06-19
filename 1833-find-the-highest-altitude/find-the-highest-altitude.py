class Solution:
    def largestAltitude(self, gains: List[int]) -> int:
        prefix_sum = [0]
        for gain in gains:
            prefix_sum.append(gain + prefix_sum[-1])

        return max(prefix_sum)