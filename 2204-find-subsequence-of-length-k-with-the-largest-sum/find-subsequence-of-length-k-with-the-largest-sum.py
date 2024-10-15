class Solution:
    def maxSubsequence(self,nums, k):
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        sorted_nums = sorted(indexed_nums, key=lambda x: x[0], reverse=True)
        
        top_k = sorted(sorted_nums[:k], key=lambda x: x[1])
        
        return [num for num, i in top_k]