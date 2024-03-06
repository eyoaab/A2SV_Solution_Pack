# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=head
   
        ref=set()
        while cur:
            if cur in ref:
                return True
            else:    
                ref.add(cur)
            cur=cur.next
   
 

        return False            
        