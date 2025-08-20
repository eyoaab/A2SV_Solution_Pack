class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        cost = 0
        
        if startPos[0] < homePos[0]:
            for r in range(startPos[0] + 1, homePos[0] + 1):
                cost += rowCosts[r]
        else:
            for r in range(startPos[0] - 1, homePos[0] - 1, -1):
                cost += rowCosts[r]
        
     
        if startPos[1] < homePos[1]:
            for c in range(startPos[1] + 1, homePos[1] + 1):
                cost += colCosts[c]
        else:
            for c in range(startPos[1] - 1, homePos[1] - 1, -1):
                cost += colCosts[c]
        
        return cost
