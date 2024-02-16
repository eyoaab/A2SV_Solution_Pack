class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while(l<r):
                currrent=nums[l]+nums[r]+nums[i]
                if abs(currrent-target)<abs(closest-target):
                     closest=currrent
                if currrent<target:
                    l+=1
                elif currrent>target:
                    r-=1
                else:
                    return currrent
        return  closest                                 
