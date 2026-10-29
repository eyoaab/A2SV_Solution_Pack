class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        masks = [1 << (ord(c) - 97) for c in s]
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        initial = masks[:]
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    initial[v] ^= initial[u]
                    stack.append(v)

        size = [1] * n
        heavy = [-1] * n
        for i in range(n - 1, 0, -1):
            u = order[i]
            p = parent[u]
            size[p] += size[u]
            if heavy[p] == -1 or size[u] > size[heavy[p]]:
                heavy[p] = u

        head = [0] * n
        for i in range(1, n):
            u = order[i]
            p = parent[u]
            head[u] = head[p] if heavy[p] == u else u

        del graph, heavy, order

        fenwick = [0] * (n + 1)

        def toggle(i: int, delta: int) -> None:
            while i <= n:
                fenwick[i] ^= delta
                i += i & -i

        def root_mask(u: int) -> int:
            result = initial[u]
            i = tin[u] + 1
            while i:
                result ^= fenwick[i]
                i -= i & -i
            return result

        answer = []
        for query in queries:
            kind, a, b = query.split()
            u = int(a)

            if kind == "update":
                new_mask = 1 << (ord(b) - 97)
                delta = masks[u] ^ new_mask
                if delta:
                    masks[u] = new_mask
                    toggle(tin[u] + 1, delta)
                    toggle(tin[u] + size[u] + 1, delta)
            else:
                v = int(b)
                x, y = u, v
                while head[x] != head[y]:
                    if depth[head[x]] > depth[head[y]]:
                        x = parent[head[x]]
                    else:
                        y = parent[head[y]]
                lca = x if depth[x] < depth[y] else y
                mask = root_mask(u) ^ root_mask(v) ^ masks[lca]
                answer.append((mask & (mask - 1)) == 0)

        return answer