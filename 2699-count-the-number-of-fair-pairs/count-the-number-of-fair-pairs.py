class Solution:
    def countFairPairs(self, arr, lower, upper):
        arr.sort()
        ans = 0

        for i in range(len(arr) - 1):
            
            low_bound = bisect_left(arr, lower - arr[i], i + 1)
            up_bound = bisect_right(arr, upper - arr[i], i + 1)
            ans += up_bound - low_bound

        return ans