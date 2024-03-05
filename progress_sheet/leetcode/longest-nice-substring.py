class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        referance=set(s)
        #print(referance)

        for index,character in enumerate(s):
            if not character.swapcase()  in referance:
                return max(self.longestNiceSubstring(s[:index]),self.longestNiceSubstring(s[index+1:]),key=len)

        return s          
        