class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        i=0
        j=0
        while( i<len(nums1) and j<len(nums2)):
            if nums1[i]< nums2[j]:
                i+=1
            elif nums2[j]< nums1[i]:
                j+=1
            else:
                ans.append(nums1[i]) 
                i+=1
                j+=1
        return ans               


        
       
                    
     

        