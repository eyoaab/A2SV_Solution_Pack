class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for i in nums:
            arr.extend(i)

        store = Counter(arr)

        answer = []
        for k, value in store.items():
            if value >= len(nums):
                answer.append(k)

        return sorted(answer) 