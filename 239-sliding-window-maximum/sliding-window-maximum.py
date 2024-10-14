class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        queue = deque()

        for index,num in enumerate(nums):
            while queue and queue[0] < index - k +1:
                queue.popleft()

            while queue and nums[queue[-1]] < num:
                queue.pop()
            
            queue.append(index)
            if index >= k - 1:
                answer.append(nums[queue[0]])     

        return answer            