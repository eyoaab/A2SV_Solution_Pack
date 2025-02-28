# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        curr = head
        maxi = 0
        while curr:
            l.append(curr.val)
            curr = curr.next
        k = len(l)-1
        left = 0
        while left < k:
            maxi = max(maxi,l[left]+l[k])
            left += 1
            k -= 1
        return maxi