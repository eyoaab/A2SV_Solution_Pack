class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        li=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    li.append(words[i])  
        li=list(set(li))
        return li                  