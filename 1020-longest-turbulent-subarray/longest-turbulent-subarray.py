class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1

        L, R, prev = 0, 1, "" 
        
        while R < len(arr):
            if arr[R] == arr[R - 1]:

                L = R
                prev = "="

            elif arr[R] > arr[R - 1] and prev != ">":

                res = max(res, R - L + 1)
                prev = ">"
            
            elif arr[R] < arr[R - 1] and prev != "<":

                res = max(res, R - L + 1)
                prev = "<"

            else:

                L = R - 1

            R += 1

        return res