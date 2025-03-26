class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        nums = []
        remainder = grid[0][0] % x
        
        for row in grid:
            for val in row:
                if val % x != remainder:
                    return -1
                nums.append(val)
        
        nums.sort()
        median = nums[len(nums) // 2]
        
        return sum(abs(num - median) // x for num in nums)