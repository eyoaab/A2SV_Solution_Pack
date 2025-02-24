class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        stores = Counter(digits)
        ans = []
        
        def dfs(length, num) -> None:
            if length == 0:
                if num % 2 == 0:
                    ans.append(num)
                return
            
            for i in range(10):
                if stores[i] == 0 or not stores[i]:
                    continue
                
                if length == 3 and i == 0:
                    continue
                    
                stores[i] -= 1
                dfs(length - 1, 10 * num + i)
                stores[i] += 1
        dfs(3, 0)
        
        return ans