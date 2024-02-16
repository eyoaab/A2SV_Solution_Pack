class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        num1=set(nums1).intersection(set(nums2))
        if len(num1)==0:
            return -1
        return min(num1)   