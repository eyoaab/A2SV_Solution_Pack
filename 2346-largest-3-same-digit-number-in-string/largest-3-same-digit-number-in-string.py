class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(1,len(num) - 1):
            if num[i] == num[i -1] == num[i + 1]:
                if ans:
                    if int(ans) < int(num[i-1:i+2]):
                        ans = num[i-1:i+2]
                else:
                    ans = num[i-1:i+2]



        return ans