class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        store = defaultdict(int)

        for i ,letter in enumerate(alphabets):
            store[letter] = weights[i]

        alphabets = alphabets[::-1]

        ans = ""

        for word in words:
            cur = 0
            for ch in word:
                cur += store[ch]

            cur = cur % 26
            ans = ans + alphabets[cur]

        return ans