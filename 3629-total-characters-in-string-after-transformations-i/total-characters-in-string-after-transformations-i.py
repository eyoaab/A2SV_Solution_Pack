class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = [0] * 26
        n, mod = len(s), int(1e9 + 7)

        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
        
        for _ in range(t):
            store = [0] * 26
            store[0] = count[25]
            store[1] = count[25]
            
            for index in range(25):
                store[index + 1] += count[index] % mod
            count = store
        
        ans = 0
        for index in range(26):
            ans += count[index] % mod
        return ans % mod