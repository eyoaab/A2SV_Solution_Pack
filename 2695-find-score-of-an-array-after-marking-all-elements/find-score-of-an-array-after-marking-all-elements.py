class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans,heap,seen,n = 0,[],set(),len(nums)

        for i,num in enumerate(nums):
            heappush(heap,(num,i))

        while heap:
            empty = False
            while True:
                if not heap: 
                    empty = True
                    break
                num,i = heappop(heap)
                if i not in seen:
                    break
                    
            if empty:
                break
            ans += num
            if i+1<n:
                seen.add(i+1)
            if i-1>=0:
                seen.add(i-1)
        return ans