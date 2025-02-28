# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        newList=None
        while(current):
            next_node=current.next
            current.next=newList
            newList=current
            current=next_node
        return newList     
        