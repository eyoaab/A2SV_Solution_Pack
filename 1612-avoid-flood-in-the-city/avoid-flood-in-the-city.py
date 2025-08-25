class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        store = defaultdict(list)
        for index,rain in enumerate(rains):
            store[rain].append(index)

        visited = set()
        heap = []
        ans = [-1 for i in range(len(rains))]

        for index,rain in enumerate(rains):
            if rain == 0:
                if heap:
                    next_index = heappop(heap)
                    if rains[next_index] in visited:
                        ans[index] = rains[next_index]
                        visited.remove(rains[next_index])
                else:
                    ans[index] = 1
            else:
                if rain in visited:
                    return []
                else:
                    visited.add(rain)
                    store[rain].pop(0)

                    if store[rain]:
                        heappush(heap, store[rain][0])

                    ans[index] = -1

        return ans