class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even=0
        for i in nums:
            if i %2==0:
                even+=i

        ans=[]
        for i,j in queries:
            k=0
            k=nums[j]+i
            if nums[j]%2==0:
                even-=nums[j]
            if k%2==0:
                    even+=k
        
            nums[j]=k
            ans.append(even)
        return ans            