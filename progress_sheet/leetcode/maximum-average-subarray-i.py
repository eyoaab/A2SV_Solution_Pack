class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        ans=s/k
        j=k
        i=0
        while(j<len(nums)):
            s+=(nums[j]-nums[i])
            ans=(max(ans,s/k))
            i+=1
            j+=1

        return ans  

            
            

        