class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        max_num  = max(nums)
        freq  = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        divisionCount = [0] * (max_num + 1)
        for g in range(1, max_num + 1):
            for multiple  in range(g, max_num + 1, g):
                divisionCount[g] += freq[multiple]
        
        exactPairs = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):

            count = divisionCount[g]
            exactPairs[g] = count * (count - 1) // 2

            for multiple in range(2 * g, max_num + 1, g):
                exactPairs[g] -= exactPairs[multiple]

        prefix = [0] * (max_num+1)
        for gcd in range(1,max_num+1):
            prefix[gcd] = prefix[gcd - 1] + exactPairs[gcd]

        ans = []
        for query in queries:
            g = bisect_left(prefix,query + 1)
            ans.append(g)

        return ans