class Solution(object):
    def countTrapezoids(self, points):
       
        M = 10**9 + 7         
        store = {}            
        
        for x, y in points:
            if y in store:
                store[y] += 1
            else:
                store[y] = 1
        
        counts = list(store.values())  
        r = 0                            
        s = 0                          
        
        for c in counts:
            if c >= 2:
                w = c * (c - 1) // 2
                
                r += w * s
                
                s += w
        
        return r % M