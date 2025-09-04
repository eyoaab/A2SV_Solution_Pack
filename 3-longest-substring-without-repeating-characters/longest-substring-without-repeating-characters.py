class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        left = 0
        ans = 0

        for right,letter in enumerate(s):
            store[letter] += 1

            while store[letter] > 1:
                store[s[left]] -= 1
                left += 1

            ans = max(ans,right - left + 1)

        return ans         