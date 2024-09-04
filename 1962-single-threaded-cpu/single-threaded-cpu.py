class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        store = []
        N = len(tasks)

        for index, task in enumerate(tasks):
            store.append(task + [index])

        store.sort(key=lambda x: x[0])
        heap = []
        inx = 0
        answer = []
        current_time = 0

        while inx < N or heap:
            while inx < N and current_time >= store[inx][0]:
                heappush(heap, (store[inx][1], store[inx][2])) 
                inx += 1

            if heap:
                processing_time, index = heappop(heap)
                answer.append(index)
                current_time += processing_time
            else:
                if inx < N:
                    current_time = store[inx][0]

        return answer
