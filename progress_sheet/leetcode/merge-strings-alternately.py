class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        fir=0
        sec=0
        merged=""
        while(fir<len(word1) and sec<len(word2)):
            merged+=word1[fir]
            fir+=1
            merged+=word2[sec]
            sec+=1
        merged+=(word1[fir:]) 
        merged+=(word2[sec:])  
        return merged  
       



