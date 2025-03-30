class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l,r,t = 0,0,0
        ans = []
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        while l < len(s):
            r = max(r,last[s[l]])
            if l == r:
                ans.append(r - t + 1)
                t = l + 1 
            l += 1
            
        return ans          

           
      
     
            
        