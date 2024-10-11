class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u - 1].append([v - 1,w])

        distances = [float('inf') for i in range(n)]

        heap = []
        heappush(heap,[0,k - 1])
        distances[k - 1]  = 0
        visited = set()

        while heap:
            curDist,curNode = heappop(heap)

            if curNode in visited:
                continue
            visited.add(curNode)     

            for child,wait in graph[curNode]:
                distance =  curDist + wait

                if distance != float('inf') and  distance < distances[child] :
                    distances[child] = distance
                    heappush(heap,[distance,child])

        if float('inf') in distances:
            return -1

        return max(distances)                    
