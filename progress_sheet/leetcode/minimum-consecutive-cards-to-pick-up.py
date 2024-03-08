class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards)==len(set(cards)):
            return -1
        ref=defaultdict(list)    
        for i in range(len(cards)):
            ref[cards[i]].append(i)
        global_min=float('inf')
        for key,val in ref.items():
            if len(val)>1:
                for i in range(len(val)):
                    for j in range(i+1,len(val)):
                        dif=val[j]-val[i]+1
                        global_min=min(global_min,dif)
        return global_min       
        
            

             




