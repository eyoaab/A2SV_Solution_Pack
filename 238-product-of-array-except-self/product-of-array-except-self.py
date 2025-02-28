class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        c=0
        ans=[]      

        for i in range(len(nums)):
            if(nums[i]==0):
                c+=1
            else:
                prod*=nums[i]
        if(c>1):
            return [0]*len(nums) 
        if(c==1):
            for i in range (len(nums)):
                if(nums[i]!=0):
                    ans.append(0)
                else:
                    ans.append(int(prod) )  
        else:            
            for i in range (len(nums)):
                if(nums[i]!=0):
                    ans.append(int(prod/nums[i]))
                else:
                    ans.append(int(prod))
                            
        return ans                