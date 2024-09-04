class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heappush(heap,[nums1[0] + nums2[1],0,0])
        visited = set((0,0))
        answer = []

        while k and heap:
            _sum,index1,index2 = heappop(heap)
            answer.append([nums1[index1], nums2[index2]])
            k -= 1

            if index1 + 1 < len(nums1):
                if not (index1 + 1,index2)  in visited:
                    heappush(heap,[nums1[index1 + 1] + nums2[index2],index1 + 1,index2])
                    visited.add((index1 + 1,index2))


            if index2 + 1 < len(nums2):
                if not (index1,index2 + 1) in visited:
                    heappush(heap,[nums2[index2 + 1] + nums1[index1],index1,index2+ + 1]) 
                    visited.add((index1,index2 + 1))


        return answer            
        

