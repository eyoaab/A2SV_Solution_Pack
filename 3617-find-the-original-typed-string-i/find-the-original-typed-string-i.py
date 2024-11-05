class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        N = len(word)
        index = 1
        while index < N:
            if word[index - 1] == word[index]: 
                count = 0
                while index < N and word[index - 1] == word[index]:
                    count += 1
                    index += 1
                ans += count    
            else:
                index += 1    
        return ans
        