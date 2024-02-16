class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst=[]
        for i in nums:
            lst+=[str(i)]
        n=len(lst)
        for i in range(n):
            for j in range(i+1,n):
                if str(lst[i])+str(lst[j])>str(lst[j])+str(lst[i]):
                    continue
                else:
                    lst[j],lst[i]= lst[i],lst[j] 
        ans="".join(lst)
        if int(ans)==0:
            return "0"
        return ans                