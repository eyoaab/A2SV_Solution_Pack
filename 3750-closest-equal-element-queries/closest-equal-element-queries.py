class Solution:
    def solveQueries(self, nums, queries):
        n = len(nums)

        mp = defaultdict(list)

        for i, val in enumerate(nums):
            mp[val].append(i)

        best = [float('inf')] * n

        for lst in mp.values():
            size = len(lst)

            if size == 1:
                best[lst[0]] = -1
                continue

            for i in range(size):
                curr = lst[i]

                prev = lst[(i - 1) % size]
                next_ = lst[(i + 1) % size]

                dist_prev = abs(curr - prev)
                dist_prev = min(dist_prev, n - dist_prev)

                dist_next = abs(curr - next_)
                dist_next = min(dist_next, n - dist_next)

                best[curr] = min(dist_prev, dist_next)

        return [best[q] for q in queries]