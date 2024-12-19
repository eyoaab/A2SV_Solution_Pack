class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = diff = 0

        for i, x in enumerate(arr):
            diff += x - i
            ans +=(diff == 0)
            
        return ans 

        