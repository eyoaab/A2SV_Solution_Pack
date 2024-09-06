# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # cur = head

        while head and head.val == val:
            head = head.next

        if not head:
            return None

        prev = head  
        cur  = head.next
        
        while cur:
            if cur.val != val:
                prev.next = cur
                prev = cur

            cur = cur.next

        prev.next = None

        return head        