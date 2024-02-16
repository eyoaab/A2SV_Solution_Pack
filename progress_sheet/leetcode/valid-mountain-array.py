class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        k=0
        pivotes=[]
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                pivotes.append(i)
        for i in pivotes:
            if (nums[:i]!=sorted(nums[:i]) or len(nums[:i])!=len(set(nums[:i])))  or (len(nums[i:])!=len(set(nums[i:])) or nums[i:]!=sorted(nums[i:],reverse=True)):
                return False
        if not pivotes or len(nums)<3:
            return False         
        return True         

        