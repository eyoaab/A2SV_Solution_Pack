class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total,current = 0, 0
        N = len(gas)
        answer = 0

        for i in range(N):
            total += gas[i] - cost[i]
            current += gas[i] - cost[i]

            if current < 0:
                answer = i + 1
                current = 0


        if total >= 0:
            return answer

        return -1            
 
        