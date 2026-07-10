class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        
        se = sorted(set(nums))

        def binse(i,val):
            j = len(se) - 1
            ans = -1
            while i<=j:
                mid = (i+j)//2
                if se[mid]==val:
                    return se[mid] 
                if se[mid]<val:
                    ans = se[mid]
                    i = mid+1
                else:
                    j = mid - 1
            return ans 
        
        binary_lift = defaultdict(lambda : -1)

        for i,j in enumerate(se):
            binary_lift[j,0] = binse(i,j+maxDiff)
        
        max_bits = len(bin(n)) - 2
        
        for i in range(1,max_bits):
            for j in se:
                binary_lift[j,i] = binary_lift[binary_lift[j,i-1],i-1]


        def get_min_dist(mi, ma):

            res = 0
            for i in range(max_bits-1,-1,-1):
                if binary_lift[mi,i]<ma:
                    res = res|(1<<i)
                    mi = binary_lift[mi,i]
                    
            
            return -1 if binary_lift[mi,0]<ma else res+1

        res = []
        for i,j in queries:
            if i==j:
                res.append(0)
                continue
            mi, ma = min(nums[i], nums[j]),max(nums[i], nums[j])
            res.append(get_min_dist(mi,ma))
        return res