class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        store = defaultdict(int)
        ans = 0

        for a,b in dominoes:
            a,b = min(a,b) , max(a,b)

            parnold = ((a + b) * (a + b + 1)) // 2 + b   
            ans += store[parnold]
            store[parnold] += 1

        
        return ans