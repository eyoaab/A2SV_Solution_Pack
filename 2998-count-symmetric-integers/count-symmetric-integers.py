class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_sym(num):
            n = len(num)
            if n % 2 != 0:
                return False

            left = 0
            right = 0

            l ,r = 0 , n - 1
            while l < r:
                left += int(num[l])
                right += int(num[r]) 

                l += 1
                r -= 1

            return left == right

        ans = 0

        for num in range(low,high + 1):
            ans += is_sym(str(num))  

        return ans            
        