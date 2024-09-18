class Solution:

    def __init__(self, head: ListNode):
        self.store = []
        curr = head

        while curr:
            self.store.append(curr)
            curr = curr.next
            
        self.length = len(self.store)

    def getRandom(self) -> int:
        index = random.randint(0, self.length - 1)
        return self.store[index].val