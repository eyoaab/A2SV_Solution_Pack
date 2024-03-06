# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left,right,best=0,n,n
        while left<=right:
            mid=left+(right-left)//2
            
            if not isBadVersion(mid):
                left=mid+1
            else:
                right=mid-1
                best=mid

        return best            

