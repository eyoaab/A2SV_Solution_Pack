class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], workers: List[int]) -> int:
        N = len(profit)
        merged = [[difficulty[i],profit[i]] for i in range(N)]
        merged.sort()

        binded_profit = [merged[i][-1] for i in range(N)]
        for i in range(1,N):
            binded_profit[i] = max(binded_profit[i],binded_profit[i - 1])

        binded_difficulty = [merged[i][0] for i in range(N)]
        answer = 0

        # print('binded profit',binded_profit)
        # print('binded_difficulty',binded_difficulty)


        for worker in workers:
            index = bisect_right(binded_difficulty,worker)
            if index != 0:
                answer += binded_profit[index - 1]
            # print(worker,index  )  


        return answer
