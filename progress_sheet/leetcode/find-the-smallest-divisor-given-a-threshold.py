class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left=1
        right=nums[-1]
        best=nums[-1]

        while left<=right:
            mid=(left+right)//2
            calculated=0
            for num in nums:
                calculated+=ceil(num/mid)

            if calculated > threshold:
                left=mid+1
            else:
                best=mid
                right=mid-1

        return best            

        