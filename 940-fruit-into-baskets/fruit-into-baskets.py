class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        _max = float('-inf')
        store = defaultdict(int)
        left = 0

        for right in range(len(fruits)):
            store[fruits[right]] += 1
            if len(store) < 3:
                ans = right - left + 1
                _max = max(_max,ans)
            else:
                while len(store) > 2 and left <= right:
                    store[fruits[left]] -= 1 
                    if store[fruits[left]] == 0:
                        store.pop(fruits[left]) 
                    left += 1
                    
        return  _max                
        