class Solution:
    def getXORSum(self, arr1, arr2):
        xor1, xor2 = 0, 0
        
        for num in arr1:
            xor1 ^= num

        for num in arr2:
            xor2 ^= num
            
        return xor1 & xor2