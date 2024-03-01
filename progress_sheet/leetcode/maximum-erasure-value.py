class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        store=set()
        max_sum=0
        left=0
        curent=0
        for i in range(len(nums)):
            if nums[i] not in store:
                curent+=nums[i]
                store.add(nums[i])
                max_sum=max(max_sum,curent)
            else:
                while nums[i] in store:
                    curent-=nums[left]
                    store.discard(nums[left])
                    left+=1
                curent+=nums[i]
                store.add(nums[i])
                max_sum=max(max_sum,curent)    
              

        return max_sum            



        