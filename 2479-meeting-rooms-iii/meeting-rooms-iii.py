class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0 for i in range(n)]

        avaliable = [i for i in range(n)]
        used = []

        for start,end in meetings:

            while used and start >= used[0][0]:
                _,room = heappop(used)
                heappush(avaliable,room)

            if not avaliable:
                new_end,room = heappop(used)
                end =  new_end + end - start
                heappush(avaliable,room)

            room = heappop(avaliable)
            count[room] += 1
            heappush(used,[end,room])

        return count.index(max(count))             