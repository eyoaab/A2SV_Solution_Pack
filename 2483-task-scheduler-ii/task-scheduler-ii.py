class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        store = {}
        day = 0

        for i in range(len(tasks)):
            task = tasks[i]
            day += 1
       
            if task in store and day - store[task] <= space:
                day += space - (day - store[task]) + 1
            
            store[task] = day
        
        return day