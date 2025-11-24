class Solution:
    def averageValue(self, nums: List[int]) -> int:
        possibles = [num for num in nums if num % 6 == 0]

        if possibles:
            return int(sum(possibles) / len(possibles))

        return 0    