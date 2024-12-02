class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li=[]
        li=sentence.split()
        for i in range(len(li)):
            if li[i].startswith(searchWord):
                return i+1
        return -1        
        