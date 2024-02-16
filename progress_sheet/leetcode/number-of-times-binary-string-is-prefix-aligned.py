class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        max_index = 0  
        for i, flip in enumerate(flips, 1):
            max_index = max(max_index, flip)
            if max_index == i: 
                ans += 1
        return ans
