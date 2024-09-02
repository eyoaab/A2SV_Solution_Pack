class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer =  {}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                topIndex = stack.pop()
                answer[nums2[topIndex]] = nums2[i]

            stack.append(i)

        saved = []
        for num in nums1:
            if num in answer:
                saved.append(answer[num])
            else:
                saved.append(-1)

        return saved        

