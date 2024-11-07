class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0

        bitB = bin(n)[2:]
        bitK = bin(k)[2:]

        if(len(bitB) < len(bitK)):
            diff = len(bitK) - len(bitB)
            bitB = '0' * diff + bitB
        if(len(bitK) < len(bitB)):
            diff= len(bitB) - len(bitK)
            bitK = '0' * diff + bitK

        count = 0
        for i in range(len(bitB)):
            if bitB[i] == '1' and bitK[i] == '0':
                count += 1
            if bitB[i] == '0' and bitK[i] == '1':
                return -1
                
        return count