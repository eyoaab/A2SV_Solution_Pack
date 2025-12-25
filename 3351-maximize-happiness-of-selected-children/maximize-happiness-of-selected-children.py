class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        counter = 0
        answer = 0
        happiness.sort(reverse = True)
        
        index = 0

        while k:
            k -= 1
            happiness[index] = max( happiness[index] - counter,0)
            answer += happiness[index]
            index += 1
            counter += 1

        return answer    