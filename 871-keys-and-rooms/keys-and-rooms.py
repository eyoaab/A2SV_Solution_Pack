class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = deque([0])
        while queue:
            n= len(queue)
            for _ in range(n):
                node = queue.popleft() 
                if node  in visited:
                    continue
                visited.add(node)
                queue.extend(rooms[node])

        return len(visited) == len(rooms)             


        