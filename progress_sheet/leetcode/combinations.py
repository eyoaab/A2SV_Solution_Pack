class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=range(1,n+1)
        ans=list(combinations(arr,k))
        return ans