class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key = lambda x:x[0]) 
        total_days = max(event[1] for event in events) 
        heap = [] 
        day, cnt, event_id = 1, 0, 0 
        
        while day <= total_days:
		  
            if event_id < len(events) and not heap:
                day = events[event_id][0]
			
            while event_id < len(events) and events[event_id][0] <= day:
                heappush(heap, events[event_id][1])
                event_id += 1 

            while heap and heap[0] < day: 
                heappop(heap) 

            if heap: 
                heappop(heap) 
                cnt += 1 
            elif event_id >= len(events): 
                break  
            day += 1 
        return cnt 