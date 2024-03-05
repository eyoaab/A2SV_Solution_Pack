# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur=head
        node=[]
        while cur:
            node.append(cur.val)
            cur=cur.next
        node.sort()
        cur=head
        for i in range(len(node)):
            cur.val=node[i]
            cur=cur.next

        return head        
        