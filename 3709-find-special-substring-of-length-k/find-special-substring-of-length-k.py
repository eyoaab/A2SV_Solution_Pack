class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        count = Counter()
        start = 0
        
        for i in range(len(s)):
            count[s[i]] += 1
            if i - start >= k:
                
                count[s[start]] -= 1
                start += 1
            left = right = False
            if count[s[i]] == k:
                if start - 1 >= 0:
                    if s[start-1] != s[i]:
                        left = True
                else:
                    left = True
                    
                if i + 1 < len(s):
                    if s[i + 1] != s[i]:
                        right = True
                else:
                    right = True
                    
           
            if left and right:
               
                return True
        return False
                    
                
        