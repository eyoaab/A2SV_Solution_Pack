class Solution(object):
    def clearStars(self, s):
        n = len(s)
        heap = []  
        m = defaultdict(deque)
        keep = [True] * n  

        for i in range(n):
            if s[i] == '*':
                smallest = heappop(heap) 
                idx = m[smallest].pop()     
                keep[i] = False            
                keep[idx] = False        
            else:
                heappush(heap, s[i])
                m[s[i]].append(i)

        return ''.join(s[i] for i in range(n) if keep[i])