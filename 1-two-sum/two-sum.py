class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {} # num,index

        for index , num in enumerate(nums):
            complment = target -  num

            if complment in store:
                return [store[complment] , index]

            store[num] = index
        return []        

