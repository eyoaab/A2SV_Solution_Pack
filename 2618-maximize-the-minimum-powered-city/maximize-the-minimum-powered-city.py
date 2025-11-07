class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        df = [0] * (n + 5)
        
        for i, j in enumerate(stations):
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j
        
        lo, hi = min(accumulate(df[:n])), 2 * 10**10

        def check(mid):
            diff = df[:]
            cur, cnt = 0, 0
            for i in range(n):
                cur += diff[i]
                if cur < mid:
                    need = mid - cur
                    cnt += need
                    if cnt > k:
                        return False
                    cur = mid
                    diff[min(n - 1, i + 2 * r) + 1] -= need
            return True

        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo