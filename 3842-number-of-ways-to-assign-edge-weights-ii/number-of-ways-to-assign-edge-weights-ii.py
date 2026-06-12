class Tree:
    def __init__(self, edges, root):
        self._depths = None
        self._parents = None
        self._precalc(edges, root)
    
    def _precalc(self, edges, root):
        vs = defaultdict(list)
        for u, v in edges:
            vs[u].append(v)
            vs[v].append(u)
        
        self._depths = depths = {}
        self._parents = parents = {}

        def dfs(node, prev, depth, path):
            path.append(node)

            parent = []
            i = 1
            while i < len(path):
                parent.append(path[-i - 1])
                i *= 2
            depths[node] = depth
            parents[node] = parent

            for next_ in vs[node]:
                if next_ == prev:
                    continue
                dfs(next_, node, depth + 1, path)
            
            path.pop()
        
        dfs(root, -1, 0, [])
    
    def get_dist(self, u, v):
        dist_u = self._depths[u]
        dist_v = self._depths[v]
        if dist_u > dist_v:
            u, v = v, u
        
        delta = abs(dist_u - dist_v)
        for pow2 in range(delta.bit_length()):
            if (delta >> pow2) & 1:
                v = self._parents[v][pow2]

        while u != v:
            p_u = self._parents[u]
            p_v = self._parents[v]
            if p_u[0] == p_v[0]:
                u = p_u[0]
                break
            for a, b in zip(reversed(p_u), reversed(p_v)):
                if a != b:
                    u, v = a, b
                    break

        return dist_u + dist_v - 2 * self._depths[u]

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        modulo = 10 ** 9 + 7
        tree = Tree(edges=edges, root=1)

        def calc(u, v):
            if u == v:
                return 0
            return pow(2, tree.get_dist(u, v) - 1, modulo)
                
        return [calc(u, v) for u, v in queries]