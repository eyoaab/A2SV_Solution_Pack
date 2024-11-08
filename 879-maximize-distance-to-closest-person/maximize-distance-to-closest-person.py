class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left,res,index = -1,0,0
        while index != len(seats):
            if left == -1 and seats[index] == 1:
                res = max(res,index)
                left = index
                index+=1
                continue
            if index == len(seats)-1 and seats[index] == 0:
                res = max(res,index-left)
                index+=1
                continue
            if seats[index] == 1:
                res = max(res,(index-left)//2)
                left = index
            index+=1
        return res
        