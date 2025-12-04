class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        
        return sum(c != 'S' for c in directions)
