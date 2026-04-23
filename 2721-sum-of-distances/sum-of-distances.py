class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        store = defaultdict(int)
        count =  defaultdict(int)
        for i, num in enumerate(nums):
            store[num] += i
            count[num] += 1

        arr = [0] * len(nums)
        n=len(nums)
        for i,num  in enumerate(nums):
            arr[i] = store[num] - count[num] * i     
            store[num] = store[num] - 2 * i
            count[num] = count[num] - 2
            
        return arr
        