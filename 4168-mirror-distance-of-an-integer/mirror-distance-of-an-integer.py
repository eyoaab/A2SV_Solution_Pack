class Solution:
    def mirrorDistance(self, n: int) -> int:
        revnum = str(n)[::-1]
        i = 0
        while i < len(revnum) and revnum[i] == "0":
            i += 1

        revnum = int(revnum[i:])

        return abs(revnum - n)     