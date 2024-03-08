class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(l=0,r=len(nums)-1,role=True):
            if l==r:
                if role:
                    return [nums[l],0] 
                else:
                     return [0,nums[l]]
            if role:
                left = helper(l+1,r, not role)
                right = helper(l,r-1, not role)
                left[0] += nums[l]
                right[0] += nums[r]
                if left[0]>=right[0]:
                    return left 
                else:
                    return right          
            else:
                left = helper(l+1,r, not role)
                right = helper(l,r-1, not role)

                left[1] += nums[l]
                right[1] += nums[r]
                if left[1]>=right[1]:
                    return left 
                else:
                    return right 
        answer=helper()            
        return answer[0]>=answer[1]
                                      