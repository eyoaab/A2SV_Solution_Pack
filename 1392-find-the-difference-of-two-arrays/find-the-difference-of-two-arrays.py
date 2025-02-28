class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        for num in nums1:
            if num not in cur and num not in nums2:
                cur.append(num)
        ans.append(cur)
        cur = []

        for num in nums2:
            if num not in cur and num not in nums1:
                cur.append(num) 
        ans.append(cur)

        return  ans         