class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0

        for word in text.split():
            isValid = True
            for broken in brokenLetters:
                if broken in word:
                    isValid = False
                    break

            if(isValid):
                ans += 1        

        return ans