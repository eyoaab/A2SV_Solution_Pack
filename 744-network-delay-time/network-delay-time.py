class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for start,end,waitght in times:
            graph[start - 1].append([end - 1,waitght])
        timeNeded = [6001 for i in range(n)]
        timeNeded[k-1] = 0

        heap = []
        heappush(heap,[0,k-1])
        visited = set()

        while heap:
            curDist , curNode = heappop(heap)

            if curNode in visited:
                continue

            visited.add(curNode)

            for child ,waight in graph[curNode]:
                time = curDist +  waight

                if time < timeNeded[child]:
                    timeNeded[child] = time
                    heappush(heap,[time,child])

        if max(timeNeded) == 6000 + 1:
            print(timeNeded)
            return -1

        return max(timeNeded)     

            
