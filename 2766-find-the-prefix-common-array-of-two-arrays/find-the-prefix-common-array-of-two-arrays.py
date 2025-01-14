class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        store = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            
            if store[A[i]] == 0:
                store[A[i]] = 1
            elif store[A[i]] == 1:
                common += 1

            if store[B[i]] == 0:
                store[B[i]] = 1
            elif store[B[i]] == 1:
                common += 1

            ans.append(common)

        return ans