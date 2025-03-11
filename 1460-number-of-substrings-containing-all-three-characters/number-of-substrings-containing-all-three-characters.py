class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        store = defaultdict(int)
        left = ans = 0

        for right in range(len(s)):
            store[s[right]] += 1
           
            while len(store) == 3:
                
                ans += len(s) - right  
                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]
                left += 1

        return ans
