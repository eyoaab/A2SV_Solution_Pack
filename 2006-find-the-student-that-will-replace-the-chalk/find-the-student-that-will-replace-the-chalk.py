class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total = sum(chalk)
        leftOver = k % total

        for index , value in enumerate(chalk):
            leftOver -= value

            if leftOver < 0:
                return index

        return 0        
