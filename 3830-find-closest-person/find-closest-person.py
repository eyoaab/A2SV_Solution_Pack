class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        distanceOfX = abs(z - x)
        distanceOfY = abs(z - y)

        if distanceOfX == distanceOfY:
            return 0
            
        elif distanceOfX < distanceOfY:
            return 1
        else:
            return 2