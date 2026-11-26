class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        is_alic = True

        while remove > 0 and n >= remove:
            n -= remove
            remove -= 1
            is_alic = not is_alic
            
        return not is_alic