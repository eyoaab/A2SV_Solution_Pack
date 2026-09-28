class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        count= 0

        for letter in s:
            if letter == "(":
                count += 1
            elif letter == ")":
                count -= 1

            ans = max(ans,count)        

        return ans
