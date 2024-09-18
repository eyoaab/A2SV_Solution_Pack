# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dummy = head

        num = ''

        while dummy:
            num += str(dummy.val)
            dummy = dummy.next

        return int(num,2)    
