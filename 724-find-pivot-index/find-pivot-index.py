class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        N = len(nums)
        pr = [0]

        for num in nums:
            pre = pr[-1]
            pr.append(pre + num)
        sum_ = pr[-1]  

        for i in range(1,N+ 1):
            left = pr[i - 1]

            if left == sum_ - pr[i]:
                return i - 1

        return -1              

   

       

        