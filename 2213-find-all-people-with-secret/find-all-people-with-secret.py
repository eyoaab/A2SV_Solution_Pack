class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        store = set([0,firstPerson])

        graph = {}

        for src,des,time in meetings:
            if time not in graph:
                graph[time] = defaultdict(list) 
            graph[time][des].append(src) 
            graph[time][src].append(des) 

        def dfs(src,neghbour):
            if src in visited:
                return
            store.add(src)
            visited.add(src)

            for neg in neghbour[src]:
                dfs(neg,neghbour)

        for t in sorted(graph.keys()):
            visited = set()

            for src in graph[t]:
                if src in store:
                    dfs(src,graph[t])

        return list(store)            

                    

