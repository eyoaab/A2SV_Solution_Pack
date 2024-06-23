class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:  
        min_que = deque()
        max_que = deque()
        start = 0
        max_len = 0

        for end in range(len(nums)):
            while min_que  and min_que[-1] > nums[end]:
                min_que.pop()
            min_que.append(nums[end])

            while max_que and max_que[-1] < nums[end]:
                max_que.pop()
            max_que.append(nums[end])

            num = max_que[0]-min_que[0]
            if num > limit:
                if nums[start] == min_que[0]:
                    min_que.popleft()
                if nums[start] == max_que[0]:
                    max_que.popleft()
                start+=1
            
            max_len = max(max_len,end - start + 1)

        return  max_len                     
                
            

           






          
                           
                                          
                               
