class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        l = []
        cur,res = 0,0
        for i in nums:
            cur+=i
            l.append(cur)
        
        for i in range(len(l)-1):
            if l[i]>=(l[-1]-l[i]):
                res+=1
        return res