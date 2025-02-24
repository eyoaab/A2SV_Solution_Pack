class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        store = Counter(s)
        ans = float('inf')
        count = Counter(target)

        for char in target:
            val = store[char] // count[char]
            ans = min(ans,val)

        return ans     
        