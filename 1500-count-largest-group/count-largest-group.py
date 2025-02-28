class Solution:
    def countLargestGroup(self, n: int) -> int:
        store = defaultdict(int)
        def returnCount(num):
            count = 0
            for i in str(num):
                count += int(i)

            return count
        
        
        for i in range(1,n + 1):
            # print(i,returnCount(i))
            store[returnCount(i)] += 1
        print(store.values()) 
        val =  list(store.values()) 
        max_ = max(val)

        return  val.count(max_) 