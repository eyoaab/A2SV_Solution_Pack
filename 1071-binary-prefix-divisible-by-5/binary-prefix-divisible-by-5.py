class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr = []
        cur = "0"
        for num in nums:
            cur += str(num)
            arr.append(int(cur,2) % 5 == 0)

        return arr    

           