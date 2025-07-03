class Solution:
    def kthCharacter(self, k: int) -> str:
        level = 0
        while (1 << level) < k:
            level += 1

        def helper(k, level):
            if level == 0:
                return 'a'

            half = 1 << (level - 1)  

            if k <= half:
                return helper(k, level - 1)
            else:
                ch = helper(k - half, level - 1)
                
                return chr(((ord(ch) - ord('a') + 1) % 26) + ord('a'))  

        return helper(k, level)