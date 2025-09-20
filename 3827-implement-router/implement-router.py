from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()
        self.dl = defaultdict(deque)
        self.exist = set()

    def removeOldest(self):
        oldest = self.q.popleft()
        self.exist.discard(oldest)
        self.dl[oldest[1]].popleft()
        return oldest

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.exist:
            return False
        if len(self.q) == self.memoryLimit:
            self.removeOldest()
        self.q.append((source, destination, timestamp))
        self.exist.add((source, destination, timestamp))
        self.dl[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            oldest = self.q.popleft()
            self.exist.discard(oldest)
            self.dl[oldest[1]].popleft()
            return list(oldest)
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        tlist = self.dl[destination]
        l = bisect_left(tlist, startTime)
        r = bisect_right(tlist, endTime)
        return r - l