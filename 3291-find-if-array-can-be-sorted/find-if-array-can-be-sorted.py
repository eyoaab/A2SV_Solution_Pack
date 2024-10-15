class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        reordered = []

        for _, item in groupby(nums, key=int.bit_count):
            reordered.extend(sorted(item))

        return all(x <= y for x, y in pairwise(reordered))