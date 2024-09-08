class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        count = 0
        
        while current:
            count += 1
            current = current.next
        
        part_size, extra_nodes = divmod(count, k)
        
        current = head
        result = []
        for i in range(k):
            part_head = current
            for j in range(part_size - 1 + (i < extra_nodes)):
                if current:
                    current = current.next
            if current:
                next_node = current.next
                current.next = None
                current = next_node
            result.append(part_head)
        
        return result
        