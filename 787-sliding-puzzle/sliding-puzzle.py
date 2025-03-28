class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"
        start = ''.join(str(num) for row in board for num in row)
        
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        queue = deque([(start, 0)]) 
        visited = set()
        visited.add(start)
        
        while queue:
            state, moves = queue.popleft()
            
            if state == target:
                return moves
            
            index = state.index('0')
            
            for neighbor in neighbors[index]:
                newMove = list(state)
                newMove[index], newMove[neighbor] = newMove[neighbor], newMove[index]
                newMove_str = ''.join(newMove)
                
                if newMove_str not in visited:
                    visited.add(newMove_str)
                    queue.append((newMove_str, moves + 1))
        
        return -1