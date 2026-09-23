class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def isThere(target,nums):
            left,right = 0 ,len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1        

            return False

        nums1.sort()
        nums2.sort()
        store1 = Counter(nums1)
        store2 = Counter(nums2)

        ans = []

        for num in nums1:
            if isThere(num,nums2) and num not in ans:
                count = min(store1[num],store2[num])
                ans.extend([num]*count)

        return ans        
        