import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.taskId_to_userId = {}
        self.taskId_to_priority = {}
        self.max_heap = []
        
        for userId, taskId, priority in tasks:
            self.taskId_to_userId[taskId] = userId
            self.taskId_to_priority[taskId] = priority
            heapq.heappush(self.max_heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """Add a new task to the system"""
        self.taskId_to_userId[taskId] = userId
        self.taskId_to_priority[taskId] = priority
        heapq.heappush(self.max_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """Update task priority using lazy deletion approach"""
        self.taskId_to_priority[taskId] = newPriority
        heapq.heappush(self.max_heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        """Remove task from system (lazy deletion from heap)"""
        if taskId in self.taskId_to_userId:
            del self.taskId_to_userId[taskId]
        if taskId in self.taskId_to_priority:
            del self.taskId_to_priority[taskId]

    def execTop(self) -> int:
        """Execute highest priority task with lazy cleanup"""
        while self.max_heap:
            priority_neg, taskId_neg = self.max_heap[0]
            taskId = -taskId_neg
            priority = -priority_neg

            if taskId not in self.taskId_to_priority:
                heapq.heappop(self.max_heap)
                continue

            if priority != self.taskId_to_priority[taskId]:
                heapq.heappop(self.max_heap)
                continue
            
            break
        
        if not self.max_heap:
            return -1

        heapq.heappop(self.max_heap)
        taskId = -self.max_heap[0][1] if self.max_heap else -(-taskId_neg)
        taskId = -taskId_neg 
        
        userId = self.taskId_to_userId[taskId]
        
        del self.taskId_to_userId[taskId]
        del self.taskId_to_priority[taskId]
        
        return userId