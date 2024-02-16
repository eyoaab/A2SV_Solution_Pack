class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        referance=sorted(nums)
        ans=[]
        for num in nums:
            ans.append(referance.index(num))
        return ans    



        