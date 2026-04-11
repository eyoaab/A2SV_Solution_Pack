class Solution:
    def minimumDistance(self, nums):
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)

        store = float('inf')

        for temp in mp.values():
            m = len(temp)

            if m >= 3:
                for i in range(m - 2):
                    a = temp[i]
                    b = temp[i + 1]
                    c = temp[i + 2]

                    diff = 2 * (c - a)
                    store = min(store, diff)

        return -1 if store == float('inf') else store