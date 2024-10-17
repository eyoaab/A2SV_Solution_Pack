class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        count = 1
        for node in preorder.split(','):
            if count <= 0:
                return False
            if node == '#':
                count -= 1
            else:
                count += 1
        return count == 0