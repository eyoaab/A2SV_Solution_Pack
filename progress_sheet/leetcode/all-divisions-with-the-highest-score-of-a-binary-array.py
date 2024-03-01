class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        store={}
        one=right_one=nums.count(1)
        zero=nums.count(0)
        store[0]=one
        store[len(nums)]=zero
        left_zero=0

        for i in range(len(nums)):
            if nums[i]==0:
                left_zero+=1
            else:
                right_one-=1
            val=left_zero+right_one    
            store[i+1]=val

        max_=max(store.values())
        return [i for i,val in store.items() if val==max_]      
