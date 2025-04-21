class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        def search(mid):
            start = mid 
            for i in range(n-1,-1,-1):
                new = start - differences[i] 
                if new > upper :
                    return  1 
                if new < lower :
                    return -1 
                start = new
            return 0 
        def find1():
            ans = -1 
            l,r = lower,upper
            while l <= r :
                mid = l + (r-l) // 2 
                res = search(mid)
                if res == 0 :
                    ans = mid 
                    r = mid - 1 
                if res == -1 :
                    l = mid + 1 
                if res == 1 :
                    r = mid - 1 
            return ans
        def find2():
            ans = -1 
            l,r = lower,upper
            while l <= r :
                mid = l + (r-l) // 2 
                res = search(mid)
                if res == 0 :
                    ans = mid 
                    l = mid + 1
                if res == -1 :
                    l = mid + 1 
                if res == 1 :
                    r = mid - 1 
            return ans
        a,b = find1(),find2()
        if a == -1 or b == -1 :
            return 0
        return b - a + 1
            