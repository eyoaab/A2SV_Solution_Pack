class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            i = 1
            cnt, ans = 0, 0
            while i * i <= x:
                if x % i == 0:
                    cnt += 1
                    ans += i
                    if i != (x // i):
                       cnt += 1
                       ans += x // i
                i += 1
            if cnt == 4:
                res += ans
        
        return res