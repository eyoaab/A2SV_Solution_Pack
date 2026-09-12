class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        new_intvl = [[val[0], val[1], val[2], ind]  for ind, val in enumerate(intervals)]
        new_intvl.sort()
    
        def find_nei(start_ind, lowerEnd):
            l = start_ind
            r = len(new_intvl) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                mid_interval_start = new_intvl[mid][0]
                if mid_interval_start > lowerEnd:
                    res = mid
                    r = mid - 1
                else:
                    l = mid + 1  
            return res
        
        base_case_result = [0, [], float('inf')]

        @lru_cache(maxsize = None)
        def maxScore(ind, k):
            if k == 0:
                return base_case_result
            if ind == len(new_intvl):
                return base_case_result

            neiInd = find_nei(ind + 1, new_intvl[ind][1])
            sub_prob_result = base_case_result if neiInd == -1 else maxScore(neiInd, k - 1)
            sub_prob_score, sub_prob_indices, sub_prob_minInd = sub_prob_result
            
            cur_score, org_ind = new_intvl[ind][2:]

            take_score = sub_prob_score + cur_score
            take_indices = [org_ind] + sub_prob_indices
            take_minInd = min(org_ind, sub_prob_minInd)
            
            no_take_score, no_take_indices, no_take_minInd = maxScore(ind + 1, k)

            take_result = [take_score, take_indices, take_minInd]
            no_take_result = [no_take_score, no_take_indices, no_take_minInd]

            if no_take_score > take_score:
                return no_take_result
            elif no_take_score < take_score:
                return take_result
            else:
                if take_minInd < no_take_minInd:
                    return take_result
                if take_minInd > no_take_minInd:
                    return no_take_result

                return take_result if sorted(take_indices) < sorted(no_take_indices) else no_take_result
        
        return sorted(maxScore(0, 4)[1])