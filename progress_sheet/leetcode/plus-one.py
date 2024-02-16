class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp=""
        for i in digits:
            temp+=str(i)
        temp=str(int(temp)+1)
        answer=[]
        for i in temp:
            answer.append(int(i))
        return answer 
        