class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        l=0
        r=len(mat)-1
        for i in (mat):
            sum+=i[l]+i[r]
            if l==r:
                sum-=i[r]
            l+=1
            r-=1
        return sum       
        