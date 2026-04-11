class Solution:
    def minimumDistance(self, nums):
        store = defaultdict(list)

        for i, num in enumerate(nums):
            store[num].append(i)

        mini = float('inf')

        for temp in store.values():
            m = len(temp)

            if m >= 3:
                for i in range(m - 2):
                    a = temp[i]
                    b = temp[i + 1]
                    c = temp[i + 2]

                    diff = 2 * (c - a)
                    mini = min(mini, diff)

        return -1 if mini == float('inf') else mini