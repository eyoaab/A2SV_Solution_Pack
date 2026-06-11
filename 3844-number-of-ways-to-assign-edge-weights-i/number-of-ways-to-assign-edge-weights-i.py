class Solution:
    MOD = 10**9 + 7

    def power(self, a, b):
        ans = 1

        while b > 0:
            if b & 1:
                ans = (ans * a) % self.MOD

            a = (a * a) % self.MOD
            b >>= 1

        return ans

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(1, 0)])  
        vis = [False] * (n + 1)

        vis[1] = True
        max_depth = 0

        while q:

            node, depth = q.popleft()

            max_depth = max(max_depth, depth)

            for neighbour in adj[node]:
                if not vis[neighbour]:
                    vis[neighbour] = True
                    q.append((neighbour, depth + 1))

        return self.power(2, max_depth - 1)