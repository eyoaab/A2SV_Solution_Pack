class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []

        ans = list(s)

        for i in ans:
            if i in "AEIOUaeiou":
                vowels.append(i)
        
        if vowels == []:
            return s

        vowels.sort()

        count = 0

        for j in range(len(s)):
            if ans[j] in "AEIOUaeiou":
                ans[j] = vowels[count]
                count += 1

        return "".join(ans)