class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_counts = Counter(nums)
        max_size = 0

        for num in num_counts:
            if num + 1 in num_counts:
                max_size = max(max_size, num_counts[num] + num_counts[num + 1])

        return max_size