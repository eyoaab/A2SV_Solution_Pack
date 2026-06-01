class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        size = len(cost)

        for i in range(0, size, 3):
            ans += cost[i]
            if i + 1 < size:
                ans += cost[i + 1]

        return ans