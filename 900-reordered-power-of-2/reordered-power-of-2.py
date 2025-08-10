class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(x):
            return ''.join(sorted(str(x)))

        target = helper(n)
        
        for i in range(31):
            if helper(1 << i) == target:
                return True
        return False