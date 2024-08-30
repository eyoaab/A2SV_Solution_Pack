class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(nums1,nums2):
            N1 , N2 = len(nums1) , len(nums2)
            best = 0

            for offset in range(N2):
                counter = 0
                for i in range(N1):
                    if i + offset >= N2:
                        break

                    if nums1[i] == nums2[i + offset]:
                        counter += 1
                        best = max(best,counter) 
                    else:
                        counter = 0

            return best  

        return max(solve(nums1,nums2),solve(nums2,nums1),)                 

