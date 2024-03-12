class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_indexes=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                one_indexes.append(i)
        #print(one_indexes)        
        answer=[0]*len(boxes)
        
        for i in range(len(boxes)):
            cur=0
            for j in range(len(one_indexes)):
                cur+=abs(one_indexes[j]-i)
            answer[i]=cur

        return answer         

        