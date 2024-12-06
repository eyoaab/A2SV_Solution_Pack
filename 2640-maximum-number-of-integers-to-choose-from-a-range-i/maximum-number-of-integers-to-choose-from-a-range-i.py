class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sum=0
        banned=set(banned)
        size=0
        for i in range(1,n+1):
            if i not in banned:
                if i+sum <= maxSum:
                    sum+=i
                    size+=1
                else:
                    break
        return size        


        