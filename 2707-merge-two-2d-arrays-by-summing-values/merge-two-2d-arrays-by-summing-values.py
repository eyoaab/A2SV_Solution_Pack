class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)

        for key, val in nums1:
            store[key] += val

        for key, val in nums2:
            store[key] += val    
            

        return sorted([[key,val] for key,val in store.items()] )