class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
            maped = {}
            def change(num):
                temp = ""
                for s in str(num):
                    temp += str(maped[int(s)])
                return int(temp)    
            for i,j in enumerate(mapping):
                maped[i] = j

            store = []
            for num in  nums: 
                store.append([change(num),num])

            store.sort(key = lambda x:x[0])
            answer = [num2 for num1,num2 in store]

            return answer   
        