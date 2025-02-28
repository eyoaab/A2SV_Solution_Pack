class Solution:
    def totalCost(self, costs, k, candidates):
        leftindex = 0
        rightIndex = len(costs) - 1
        leftCandidate = []
        rightCandidate = []

        ans = 0
        while k > 0:

            while len(leftCandidate) < candidates and leftindex <= rightIndex:
                heapq.heappush(leftCandidate, costs[leftindex])
                leftindex += 1
            while len(rightCandidate) < candidates and leftindex <= rightIndex:
                heapq.heappush(rightCandidate, costs[rightIndex])
                rightIndex -= 1

            const1 = leftCandidate[0] if leftCandidate else float('inf')
            const2 = rightCandidate[0] if rightCandidate else float('inf')

            if const1 <= const2:
                ans += const1
                heapq.heappop(leftCandidate)
            else:
                ans += const2
                heapq.heappop(rightCandidate)

            k -= 1
        return ans