# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd=[]
        cur=head
     
        while cur:
            odd.append(cur.val)
            if cur.next:
                cur =cur.next.next
            else:
                break 
        cur=head.next
        while cur:
            odd.append(cur.val)
            if cur.next:
                cur =cur.next.next
            else:
                break
        cur=head
    
        for od in odd:
            cur.val=od
            cur=cur.next

      
        return head   