class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiop"
        second="asdfghjkl"
        third="zxcvbnm"
        ans=[]
        for word in words:
            if all(i.lower() in first for i in word):
                ans.append(word)
            if all(i.lower() in second for i in word):
                ans.append(word)
            if all(i.lower() in third for i in word):
                ans.append(word)
        return ans                
        