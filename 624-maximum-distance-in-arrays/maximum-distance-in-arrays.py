class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minindex,minval = 0,arrays[0][0]
        maxindex,maxval = 0,arrays[0][-1]



        for idx in range(1,len(arrays)):
            arr = arrays[idx]
            if arr[-1 ] > maxval:
                maxval = arr[-1]
                maxindex = idx

            if arr[0 ] < minval:
                minval = arr[0]
                minindex = idx    

        ans = float("-inf")
        print(minindex,maxindex)
        for i,num in enumerate(arrays):
            if i != maxindex:
                ans = max(ans,abs(maxval - num[0]))  
            if i != minindex:
                ans = max(ans,abs(minval - num[-1]))     

        return ans                   