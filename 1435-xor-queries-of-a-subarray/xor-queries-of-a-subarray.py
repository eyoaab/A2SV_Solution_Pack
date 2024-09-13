class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        prefix = [0 for i in range(N)]
        answer = []

        prefix[0] = arr[0]

        for i in range(1,N):
            prefix[i] = arr[i] ^ prefix[i - 1]

        for left,right in queries:
            if left == 0:
                answer.append(prefix[right])
            else:
                answer.append(prefix[right] ^  prefix[left - 1])        

        # answer = []
        return answer    

        