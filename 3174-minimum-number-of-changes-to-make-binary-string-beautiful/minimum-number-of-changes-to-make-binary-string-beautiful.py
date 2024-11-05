class Solution:
   def minChanges(self,s):
        count = 0
        i = 0
        N = len(s) - 1

        while i < N:
            if s[i] != s[i + 1]:
                count += 1
            i += 2

        return count