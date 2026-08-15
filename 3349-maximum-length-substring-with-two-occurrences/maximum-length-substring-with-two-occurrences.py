class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        referance = defaultdict(int)
        left = answer = 0
        
        for right in range(len(s)):
            if referance[s[right]] == 2:
                while referance[s[right]] == 2:
                    referance[s[left]] -= 1
                    if  referance[s[left]] == 0:
                        del  referance[s[left]]
                    left += 1 
            referance[s[right]] +=1          
            answer = max(answer,right - left +1)
        return answer     
            