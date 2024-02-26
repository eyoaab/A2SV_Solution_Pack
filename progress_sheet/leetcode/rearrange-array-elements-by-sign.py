class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posetive=[]
        negative=[]
        for num in nums:
            if num >0:
                posetive.append(num)
            else:
                negative.append(num) 
        posetive=posetive[::-1]
        negative=negative[::-1]
        answer=[]
        for i in range(len(posetive)):
             answer.append(posetive.pop())
             answer.append(negative.pop())
        return answer     


        