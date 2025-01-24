class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        color =[0 for i in range(len(graph))]

       
        def dfs(node):
            if color[node] == 1:
                return False
            color[node] = 1
            temp = True
            for neg in graph[node]:
                if color[neg] == 2:
                    continue
                temp =  temp and dfs(neg)
            if temp:        
                color[node] = 2
                answer.append(node)
                return True
            return temp    

        for i in range(len(graph)):
            if color[i] != 0:
                continue
            dfs(i)
               
        return sorted(answer)                     