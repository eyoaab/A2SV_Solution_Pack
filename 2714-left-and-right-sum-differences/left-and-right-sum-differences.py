class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        ans = []

        for num in nums:
            if left:
                left.append(left[-1] +  num)
            else:
                left.append(num)
                    
        for num in nums[::-1]:
            if right:
                right.append(right[-1] +  num)
            else:
                right.append(num)

        right = right[::-1]

        for i in range(len(nums)):
            ans.append(abs(right[i] - left[i]))

        return ans              