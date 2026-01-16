class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        mod = 10**9 + 7
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        hashSet = set()
        
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                hashSet.add(h[j] - h[i])

        ans = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in hashSet:
                    if d > ans:
                        ans = d

        if ans == -1:
            return -1
        return (ans ** 2) % mod
                        