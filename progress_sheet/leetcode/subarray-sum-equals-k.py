class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        count=0
        temp=defaultdict(int)
        for i in range(len(nums)):
            sum+=nums[i]
            if sum==k:
                count+=1
            if (sum-k) in temp:
                count+=temp[sum-k]
            temp[sum]+=1
        return count           

        