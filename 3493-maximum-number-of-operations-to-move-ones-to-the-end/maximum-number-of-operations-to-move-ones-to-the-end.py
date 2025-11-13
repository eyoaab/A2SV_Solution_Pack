class Solution:
    def maxOperations(self, s: str, res = 0, cnt = 0) -> int:

        for num in list(map(len,s.split('0'))):

            if num == 0: continue
            cnt+= num
            res+= cnt

        return res if num == 0 else res - cnt