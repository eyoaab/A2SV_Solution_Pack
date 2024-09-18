class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        store, c, flag = set(nums), 0, False

        while(head):
            if head.val in store:
                flag = True
            elif flag:
                c += 1
                flag = False
            head = head.next

        return c + 1 if flag else c