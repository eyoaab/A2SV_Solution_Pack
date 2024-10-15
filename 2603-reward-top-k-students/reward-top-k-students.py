class Solution:
    def topStudents(self, positive: List[str], negative: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive=set(positive)
        negative=set(negative)
        heap=[]
        for i in range(len(student_id)):
            c=0
            b="".join(report[i]).split(" ")
            for j in b:
                if j in positive:
                    c+=3
                elif j in negative:
                    c-=1
            heappush(heap,[-c,student_id[i]])
        res=[]
        while k:
            l=heappop(heap)
            res.append(l[1])
            k-=1
        return res