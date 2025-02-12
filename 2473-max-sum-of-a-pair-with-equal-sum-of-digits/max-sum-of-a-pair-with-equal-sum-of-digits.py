class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def getDigit(num):
            ans = 0
            for n in str(num):
                ans += int(n)

            return ans

        store = defaultdict(list)
        for num in nums:
            store[getDigit(num)].append(num)

        ans = -1
        for _,array in store.items():
            lis = array
            cur = 0
            if len(lis) > 1:
                cur += lis.pop((lis.index(max(lis))))
                cur += lis.pop((lis.index(max(lis))))
                ans = max(ans,cur)    
                
        return ans
