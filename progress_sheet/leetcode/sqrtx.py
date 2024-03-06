class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x

        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                right=mid-1  
            else:
                left=mid+1
            #print(left)
        return left-1              

        