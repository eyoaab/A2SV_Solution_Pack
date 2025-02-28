class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        sorted_indices = sorted(range(len(nums2)), key=lambda i: nums2[i])

        nums1_sorted = [nums1[i] for i in sorted_indices]
        nums2_sorted = [nums2[i] for i in sorted_indices]
        n = len(nums2)

        rest = nums1_sorted[n - k:]

        sum_rest = sum(rest)
        heapq.heapify(rest)
        res = nums2_sorted[n - k] * sum_rest

        for i in range(n - k - 1, -1, -1):
            sum_rest += nums1_sorted[i]
            sum_rest -= heapq.heappushpop(rest, nums1_sorted[i])
            res = max(res, nums2_sorted[i] * sum_rest)
        
        return res