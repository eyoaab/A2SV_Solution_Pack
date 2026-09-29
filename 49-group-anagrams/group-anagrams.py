class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        store = {}
        for sr in strs:
            word = "".join(sorted(sr))
            if word in store:
                store[word].append(sr)
            else:
                store[word] = []   
                store[word].append(sr)

        ans = []
        for key,val in store.items():
            ans.append(val) 
        return ans         
