class Solution:
    def isCovered(self, ranges, left, right):
        ans = [False] * (right + 1)
        ans[0] = True
       
        for r in ranges:
            for i in range(r[0], r[1]+1):
                if i<=right and i>=left:
                    ans[i] = True
        for i in range(left, right + 1):
            if not ans[i]:
                return False
        return True
