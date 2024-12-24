class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diameter(edges):
            n = len(edges)+1
            degree = [0] * n
            adjecent = [[] for _ in range(n)]
            for v, w in edges:
                adjecent[v].append(w)
                adjecent[w].append(v)
                degree[v] += 1
                degree[w] += 1
            queue=deque()
            for i, d in enumerate(degree):
                if d == 1:
                    queue.append(i)
            level, left = 0, n
            while left > 2:
                queuez = len(queue)
                left -= queuez
                for i in range(queuez):
                    v = queue.popleft()
                    for w in adjecent[v]:
                        degree[w] -= 1
                        if degree[w] == 1:
                            queue.append(w)
                level += 1
            return 2 * level + 1 if left == 2 else 2 * level

        d1 = diameter(edges1)
        d2 = diameter(edges2)

        return max(d1, d2, (d1+1)//2+(d2+1)//2+1)
        
        