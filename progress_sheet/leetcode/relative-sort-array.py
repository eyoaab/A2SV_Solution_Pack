class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        left = []
        ans = []
        for i in arr1:
            if i not in arr2:
                left.append(i)
        left.sort()
        mydict = dict(Counter(arr1))
        for i in arr2:
            while mydict[i]:
                ans.append(i)
                mydict[i] -= 1
        ans.extend(left)
        return ans