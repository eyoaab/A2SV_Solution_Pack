class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        xor = 0

        for num in nums:
            xor ^= num
            k = 0

            for i in range(maximumBit):
                if xor & 1 << i == 0:
                    k |= 1 << i
            answer.append(k)

        return answer[::-1]   


        

        