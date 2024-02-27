class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=dict(Counter(arr).most_common())
        for i,j in count.items():
            if j>=len(arr)//4:
                return i
        return 0        
        