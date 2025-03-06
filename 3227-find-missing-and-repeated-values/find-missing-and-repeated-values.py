class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        elements = []

        for elem in grid:
             for i in elem:
                 elements.append(i)

        missed = 0
        reapetted = 0

        for i in range(1 , n +  1):
            
            if  elements.count(i) == 2:
                reapetted = i
            if  elements.count(i) == 0:
                    missed = i

        return [reapetted,missed]            
  




        