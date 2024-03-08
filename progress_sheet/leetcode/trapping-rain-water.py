class Solution:
    def trap(self, height: List[int]) -> int:
        out = 0
        
        max_left, max_right = height[0], height[-1]
        i, j = 1, len(height) - 2
        
        while i <= j:
            max_left = max(max_left, height[i])
            max_right = max(max_right, height[j])
            if max_left < max_right:
                out += max_left - height[i]
                i += 1
            else:
                out += max_right - height[j]
                j -= 1
        
        return out
