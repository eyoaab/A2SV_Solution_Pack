# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp1,temp2=head,head.next
        while temp2:
            while temp2 and temp1.val==temp2.val:
                temp2=temp2.next
            temp1.next=temp2
           
            if temp2:
                temp1=temp2
                temp2=temp2.next
            else:
                temp1.next=None


        return head     

           


        
        