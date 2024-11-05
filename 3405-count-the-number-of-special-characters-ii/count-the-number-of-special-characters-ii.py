class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        lowwer = {}
        upper = {}

        for i,s in enumerate(word):
            if s.islower():
                lowwer[s] = i

        for i in range(len(word) - 1,-1,-1):
            s = word[i]
            if s.isupper():
                upper[s] = i    

        for i,s in enumerate(set(word)):
            if s.isupper():
                if s.lower() in lowwer:
                    if upper[s] > lowwer[s.lower()]:
                        ans += 1

         

        return ans        
                