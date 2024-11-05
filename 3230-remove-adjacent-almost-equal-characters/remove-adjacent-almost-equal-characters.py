class Solution:
    def helper(self,a,b):
        return a == b or abs(ord(a) - ord(b)) == 1
       
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i = 0
        n = len(word) - 1
        word = list(word)
        ans = 0

        while i <= n - 1:
            if self.helper(word[i] , word[i+1]):
                word[i+1] = "~"
                ans += 1
            i += 1

        return ans