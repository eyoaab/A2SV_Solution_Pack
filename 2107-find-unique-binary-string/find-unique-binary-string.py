class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        length = 2 ** n

        nums = [int(num,2) for num in nums]

        for i in range(length):
            if i not in nums:
                need = n - len(str(bin(i))[2:])
                return need * '0' + str(bin(i))[2:]


        return ''        