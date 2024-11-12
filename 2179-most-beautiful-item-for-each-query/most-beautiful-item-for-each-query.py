class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        store = defaultdict(int)

        for price,beauty in items:
            store[price] = max(store[price],beauty)
        values = [[i,j] for i,j in store.items() ] 
        values = sorted(values,key=lambda x:x[0])

        for i in range(1,len(values)):
            store[values[i][0]] = max(store[values[i][0]],store[values[i- 1][0]])


        candidates = sorted(store.keys())
        

        answer = [] 

        for query in queries:
            val = bisect_right(candidates,query)
            if val == 0:
                answer.append(0)
            else:    
                best = store[candidates[val - 1]]

                # val =  binary_serch(query)
                answer.append(best)   

        return answer             


        