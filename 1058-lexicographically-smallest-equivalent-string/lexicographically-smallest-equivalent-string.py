class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        st = 'abcdefghijklmnopqrstuvwxyz'
        store = {s:s for s in st}

        def find(s):
            return store[s]

        def union(st1,st2):
            rep1 = find(st1)
            rep2 = find(st2)
            if st1 == st2:
                return

            if rep1 < rep2:
                for i,j in store.items():
                    if j ==  rep2:
                        store[i] = rep1
            if rep1 > rep2:
                   for i,j in store.items():
                    if j ==  rep1:
                        store[i] = rep2
        for i in range(len(s1)):
            union(s1[i],s2[i]) 
        answer = ""
        for s in baseStr:
            answer +=find(s)
        return answer                       

