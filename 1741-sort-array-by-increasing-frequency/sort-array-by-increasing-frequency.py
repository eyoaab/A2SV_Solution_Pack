class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=dict(Counter(nums).most_common())
        return sorted(nums, key=lambda x: (-count[x], x))[::-1]  
        