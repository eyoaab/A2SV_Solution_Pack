class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        referance={}
        for i in range(len(order)):
            referance[order[i]]=i
        result=[]
        for word in words:
            indexes=[]
            for char in word:
                indexes.append(referance[char])
            result.append(indexes)

        return sorted(result)==result        

        
        print(referance)
        return True