# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nodes=[]
        cur=head

        while cur:
            nodes.append(cur.val)
            cur=cur.next
        first=[]
        second=[]
        for node in nodes:
            if node<x:
                first.append(node)
            else:
                second.append(node)
        answer=first+second
        dummy=ListNode()
        cur=dummy
        for ans in answer:
            temp=ListNode(ans)
            cur.next=temp
            cur=cur.next
        return dummy.next

                 
        