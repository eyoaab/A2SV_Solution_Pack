class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[]
        new_list=[]
        for a,b in costs:
            diff=b-a
            temp=[a,b,diff]
            new_list.append(temp)
        new_list.sort(key=lambda x:(x[2]),reverse=True)
        total=0
        for i in new_list[:len(new_list)//2]:
            total+=i[0]
        for i in new_list[len(new_list)//2:]:
            total+=i[1] 
        return total          


