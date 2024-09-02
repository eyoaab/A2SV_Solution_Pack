class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        store =set()
        if len(s) < k:
            return False

        right = k - 1
        left = 0

        while right < len(s):
            store.add(s[left:right + 1])
            left += 1
            right += 1

        return len(store) == 2 ** k