# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        index = 0
    
        stack = []
        answer = {}

        cur = head

        while cur:
            val = cur.val

            while stack and stack[-1][-1] < val:
                place,num = stack.pop()
                answer[place] = val

            stack.append([index,val])  
            index += 1
            cur = cur.next  

        for place,_ in stack:
            answer[place] = 0


        result = [0 for i in range(len(answer))]  

        for place,num in answer.items():
            result[place] = num
        return result      