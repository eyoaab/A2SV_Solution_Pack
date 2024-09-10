class Solution:
    def reorderSpaces(self, text: str) -> str:

        space = text.count(" ")
        words = text.split()
        N = len(words)

        if N-1 > 0:
            spaceAmount = space//(N-1)
        else:
            spaceAmount = space
        
        ans = ""
        for word in words:
            ans += word
            if space >= spaceAmount:
                ans += " " * spaceAmount
                space -= spaceAmount
        
        if space > 0:
            ans += " " * space
        
        return ans