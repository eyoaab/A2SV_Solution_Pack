class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        # first_path=0
        # second_path=0

        # for i in range(start,end):
        #     i=i%len(distance)
        #     first_path+=distance[i]

        # for i in range(end,len(distance)+start):
        #     i=i%len(distance)
        #     second_path+= distance[i]

        
        # res =  min(first_path,second_path) 
        # return res if res !=0 else max(first_path,second_path)   
        total = sum(distance)
        path1 = sum(distance[start: end]) if start < end else sum(distance[end: start])
        path2 = total - path1
        return min(path1, path2) 


        