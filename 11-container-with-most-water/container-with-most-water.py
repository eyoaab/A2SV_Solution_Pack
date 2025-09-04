class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left ,right = 0, len(heights) - 1

        while left < right:
            height = min(heights[right], heights[left]) 
            width =  right - left
            area = width * height
            ans = max(ans,area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans            