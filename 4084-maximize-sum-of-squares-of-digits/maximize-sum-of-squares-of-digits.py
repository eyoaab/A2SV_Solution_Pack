class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = ""

        while sum > 0:
            if sum > 9:
                ans += "9"
                sum -= 9
            else:
                ans += str(sum)
                break    

        if len(ans) > num:
            return ""
        left = num - len(ans) 
        ans += "0" * left   

        return ans 