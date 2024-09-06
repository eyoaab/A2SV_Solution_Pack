# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        free_nodes = []
        nums = set(nums)

        cur = head

        while cur:
            if cur.val not in nums:
                free_nodes.append(cur.val)

            cur = cur.next

        dummy =  ListNode()
        cur = dummy

        for num in free_nodes:
            temp  = ListNode(num)
            cur.next = temp
            cur = cur.next

        return dummy.next           