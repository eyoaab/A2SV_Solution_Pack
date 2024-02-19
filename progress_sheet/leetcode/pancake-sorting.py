class Solution:
    def pancakeSort(self, given: List[int]) -> List[int]:
        arr=given
        answer = []
        while len(arr)>0:
            index=arr.index(max(arr))
            if index==0:
                answer.append(len(arr))
                arr.reverse()
                arr.pop()
            elif index==len(arr)-1:
                arr.pop()
            else:
                answer.append(index+1)
                arr=arr[index::-1]+arr[index+1::]
        return answer               
        