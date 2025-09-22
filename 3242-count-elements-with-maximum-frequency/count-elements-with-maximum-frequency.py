class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        store = max(count.values())
        answer = 0
        
        for key,value in count.items():
            if value == store:
                answer += 1

        return answer * store        
        