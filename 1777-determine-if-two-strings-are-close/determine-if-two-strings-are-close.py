class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False
         
        count1=dict(Counter(word1).most_common())  
        count2=dict(Counter(word2).most_common())
        for i in count1.keys():
            if i not in word2:
                return False
        for i in count2.keys():
            if i not in word1:
                return False          
        val1=sorted(count1.values())
        val2=sorted(count2.values())
        return val1==val2 

        