class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums2 = Counter(nums2)

        for num in nums1:
            if num in nums2:
                answer.append(num)
                nums2[num] -= 1

                if nums2[num] == 0:
                    del nums2[num]        

        return answer         