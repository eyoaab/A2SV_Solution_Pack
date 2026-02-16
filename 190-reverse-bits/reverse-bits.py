class Solution:
    def reverseBits(self, n: int) -> int:
          bitNum = bin(n)[2:]
          addedZeros = 32 - len(bitNum)
          bitNum = bitNum[::-1] + ("0" * addedZeros)
          return int(bitNum,2)