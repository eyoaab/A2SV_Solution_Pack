class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        n = len(s)
        store = defaultdict(int)

        for right in range(n):
            store[s[right]] += 1

            while store[s[right]] > 1 and left < right:
                store[s[left]] -= 1
                left += 1

            currentMax = right - left + 1
            answer = max(answer, currentMax)    

        
        return answer