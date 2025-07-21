class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        store = Counter(chars)

        ans = 0
        for word in words:
            cur = Counter(word)
            isFul = True
            for i,j in cur.items():
                if i not in store.keys() or j > store[i]:
                    isFul = False
                    break

            if isFul:
                ans += len(word)        

                

        return ans