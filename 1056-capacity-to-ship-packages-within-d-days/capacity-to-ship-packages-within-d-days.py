class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right,best = max(weights),sum(weights), - 1

        while left <= right:
            mid = (left + right) // 2

            daycount = 1
            waightcount = 0

            for i in range(len(weights)):
                waightcount += weights[i]
                if waightcount > mid:
                    waightcount = weights[i]
                    daycount += 1

            if  (daycount) >  days:
                left = mid + 1
            else:
                best = mid
                right = mid - 1  

        return best             

