class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallest = 1
        multiple_of_k = set()

        for num in nums:
            if num % k == 0:
                multiple_of_k.add(num // k)

            if num // k == smallest:
                while smallest in multiple_of_k:
                    smallest += 1

        return smallest * k