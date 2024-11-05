class Solution:
    def bestClosingTime(self, customers: str) -> int:
        allY = customers.count('Y')
        allN = customers.count('N')

        N = len(customers)

        curN = 0

        store = [N for i in range(N + 1)]

        for index,char in enumerate(customers):
            store[index] = allY + curN

            if char == 'Y':
                allY -= 1
            else:
                curN += 1
        store[N]  =  allN
        # print(store)

        return store.index(min(store))     





        