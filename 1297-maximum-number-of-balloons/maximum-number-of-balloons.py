class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        store = Counter(text)
        ans = float('inf')
        
        ans = min(ans,store['b'])
        ans = min(ans,store['a'])
        ans = min(ans,store['l'] // 2)
        ans = min(ans,store['o'] // 2)
        ans = min(ans,store['n'])

        return ans