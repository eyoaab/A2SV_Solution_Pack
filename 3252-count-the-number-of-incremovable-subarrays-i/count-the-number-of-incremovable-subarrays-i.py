class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        answer = 0

        for left in range(len(nums)):
            for right in range(left,len(nums)):
                newArray = nums[:left] + nums[right + 1:]
                valid = True

                for i in range(len(newArray) - 1):
                    if newArray[i] < newArray[i + 1]:
                        valid = True
                    else:
                        valid = False
                        break

                if valid:
                    answer += 1

        return answer                        
