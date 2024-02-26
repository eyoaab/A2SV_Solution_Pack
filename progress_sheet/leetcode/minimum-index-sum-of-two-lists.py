class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        temp=list(set(list1).intersection(set(list2)))
        mi=10000000000
        for i in temp:
            mi=min( list1.index(i)+list2.index(i),mi)

        for i in temp:
            if list1.index(i)+list2.index(i) ==mi:
                ans.append(i)
        return ans
        