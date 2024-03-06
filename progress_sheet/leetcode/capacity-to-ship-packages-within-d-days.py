class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right,best=max(weights),sum(weights),-1

        while left<=right:
            mid_weight=left + (right-left)//2

            calculate_days=1
            counter=0
            for i in range(len(weights)):
                counter += weights[i]
                if mid_weight < counter:
                    counter = weights[i]
                    calculate_days += 1

            if calculate_days > days:
               left = mid_weight+1
            else:
                right=mid_weight -1
                best = mid_weight

        return best           



            