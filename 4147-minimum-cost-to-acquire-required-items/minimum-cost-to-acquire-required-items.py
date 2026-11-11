class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2:
            return self.minimumCost(cost2, cost1, costBoth, need2, need1)

        collectBoth = need1 * min(costBoth, cost1 + cost2)

        collectRem = (need2 - need1) * min(cost2, costBoth)

        return collectBoth + collectRem