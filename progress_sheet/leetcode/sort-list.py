# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        cur=head
        if not head:
            return head
       
        while cur:
            ans.append(cur.val)
            cur=cur.next
        ans.sort()    
        root= head
        for i in range(len(ans)):
            root.val=ans[i]
            root=root.next 
        return head     