class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        store = defaultdict(list)
        for index,rain in enumerate(rains):
            store[rain].append(index)

        full = set()
        heap = []
        ans = []

        for index,rain in enumerate(rains):
            if rain == 0:
                if heap:
                    next_index = heappop(heap)
                    if rains[next_index] in full:
                        ans.append(rains[next_index])
                        full.remove(rains[next_index])
                else:
                    ans.append(1)
            else:
                if rain in full:
                    return []
                else:
                    full.add(rain)
                    store[rain].pop(0)

                    if store[rain]:
                        heappush(heap, store[rain][0])

                    ans.append(-1)

        return ans