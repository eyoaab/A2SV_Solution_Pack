class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots = []
        left = []
        right = []

        for num in nums:
            if  num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                pivots.append(num)

        return left + pivots + right                 