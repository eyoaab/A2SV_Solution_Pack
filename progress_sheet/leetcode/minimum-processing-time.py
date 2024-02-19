class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        result=0
        index=0
        for i in range(0,len(tasks)-3,+4):
            result=max(result,tasks[i]+processorTime[index])
            index+=1
        return result    
        