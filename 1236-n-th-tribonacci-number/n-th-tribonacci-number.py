class Solution:
    def tribonacci(self, n: int) -> int:

        store =  {1:1,0:0,2:1}
        
        def solve(n):
            if n not in store:
                store[n] = solve(n - 1) + solve(n - 2) + solve(n - 3)

            return store[n]

        return solve(n)                