class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairs = [i for i in range(len(times) + 1)]
        

        times = [[time[0],time[1],index] for index,time in enumerate(times)]
        heap = []
        times.sort()
        print(times)

        for start,end,friend in times:
            while  heap and heap[0][0] <= start:
                _,chair = heappop(heap)
                heappush(chairs,chair)

            if friend == targetFriend:
                return heappop(chairs)

            heappush(heap,[end,heappop(chairs)]) 
        return -1          
