
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = Counter(nums)
        
        for num, freq in count.items():
            if freq > len(nums) // 3:
                ans.append(num)
                
        return ans
