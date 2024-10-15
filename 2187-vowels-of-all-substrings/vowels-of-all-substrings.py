class Solution:
    def countVowels(self, word: str) -> int:
        vowel = 0
        vowels = 'aeiou'

        for i,v in enumerate(word):
            if v in vowels:
                vowel += (i + 1 )* (len(word)-i)

        return vowel