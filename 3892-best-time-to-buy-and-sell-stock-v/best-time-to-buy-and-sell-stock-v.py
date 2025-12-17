class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @lru_cache(maxsize=1000*4)
        def dps(i, lf, kd):
            # array or capacity is over
            if i >= len(prices) or lf == 0:
                # if we finished with a pending operation return -inf
                return 0 if kd==-1 else -inf
            
            mx = -inf
            if kd > -1:
                if kd == 0:
                    # buy, because we sold
                    mx = dps(i+1, lf-1, -1)  - prices[i]
                else:
                    # sell, because we bought
                    mx = dps(i+1, lf-1, -1)  + prices[i]
            else:
                # sell or buy
                mx = max(dps(i+1, lf, 0)  + prices[i],
                            dps(i+1, lf, 1)  - prices[i])
            # do nothing
            return max(dps(i+1, lf, kd), mx)
        
        return dps(0, k, -1)