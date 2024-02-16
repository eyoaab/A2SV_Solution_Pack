class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort(key=lambda x:(x==2,x==1,x==0))
       