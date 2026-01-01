class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strnum = ''
        for digit in digits:
            strnum += str(digit)

        intNum = int(strnum) + 1
        strnum = str(intNum)

        ans = []
        for s in strnum:
            ans.append(int(s))

        return ans    
        