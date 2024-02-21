class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer=0

        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                continue
        
            no_of_ele=ceil(nums[i]/nums[i+1])
            answer+= no_of_ele-1
            nums[i]=nums[i]//no_of_ele

        return answer
        