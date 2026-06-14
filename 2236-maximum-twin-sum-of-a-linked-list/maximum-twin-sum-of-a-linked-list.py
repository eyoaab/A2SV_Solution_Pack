# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        node = head
        while node:
            arr.append(node.val)
            node = node.next

        ans = 0

        left, right = 0 , len(arr) - 1
        while left < right:
            cur = arr[left] + arr[right]
            ans = max(ans,cur)
            left += 1
            right -= 1

        return ans        