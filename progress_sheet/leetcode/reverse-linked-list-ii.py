# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        answer=[]
        current=head
        while current:
            answer.append(current.val)
            current=current.next
        answer=answer[:left-1]+answer[left-1:right][::-1]+answer[right:]
        current=head
        for ans in answer:
            if current:
                current.val=ans
                current=current.next
        return head    

        