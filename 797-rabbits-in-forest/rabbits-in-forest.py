class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        referance=dict(Counter(answers))
        result=0
        for i,j in referance.items():
            result+=(i+1)*ceil(j/(i+1))
        return result    


        