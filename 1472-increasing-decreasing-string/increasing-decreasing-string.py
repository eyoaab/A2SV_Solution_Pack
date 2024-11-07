class Solution:
    def sortString(self, s: str) -> str:
        store = Counter(s)
        key_store = sorted(store.keys())
        answer = ''

        while len(answer) < len(s):

            for i in key_store:
                if store[i] > 0: 
                    answer, store[i] = answer + i, store[i] - 1
            for i in key_store[::-1]:
                if store[i] > 0: 
                    answer, store[i] = answer + i, store[i] - 1
                    
        return answer