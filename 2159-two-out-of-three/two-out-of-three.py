class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        store = {}
        ans = []
        for i in nums1:
           store[i] = 1
        for i in nums2:
            if i in store:
                if i not in ans:
                    ans.append(i)
        for i in nums3:
            if i in store:
                if i not in ans:
                    ans.append(i)
        
        store = {}
        for i in nums3:
            store[i] = 1
        for i in nums2:
            if i in store:
                if i not in ans:
                    ans.append(i)
        return ans