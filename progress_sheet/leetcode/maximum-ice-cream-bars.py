class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer=0
        costs.sort()
        for i in costs:
            if coins<i:
                break
            else:
                answer+=1
                coins-=i
        return answer

        