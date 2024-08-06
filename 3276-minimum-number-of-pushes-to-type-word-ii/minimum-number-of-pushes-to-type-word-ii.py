class Solution:
    def minimumPushes(self, word: str) -> int:
        store = Counter(word)
        val = sorted(store.values(), reverse=True)

        i = 1
        ans = 0
        count = 0

        for num in val:
            ans += (i * num)
            count += 1

            if count == 8:
                count = 0
                i += 1

        return ans
