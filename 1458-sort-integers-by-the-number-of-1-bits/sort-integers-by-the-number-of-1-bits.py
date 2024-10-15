class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOne(num):
            return bin(num).count('1')

        binded =[ [num,countOne(num)] for num in arr]

        binded.sort(key = lambda x:(x[1],x[0]))

        return [num for num,_ in binded]   