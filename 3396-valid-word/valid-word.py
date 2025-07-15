class Solution:
    def isValid(self, word: str) -> bool:
        voules = "aeiou"
        digits = "1234567890"
        consonents = "bcdfghjklmnpqrstvwxyz"    

        voul, digit, consonent = 0,0,0,

        if len(word) < 3:
            return False

        for letter in word:
            if letter in digits:
                digit += 1
            elif letter.lower() in voules:
                voul += 1
            elif letter.lower() in consonents:
                consonent += 1
            else:
                return False   

        if voul == 0 or consonent == 0:
            return False

        return True                      

