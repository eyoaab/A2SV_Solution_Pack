class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_half, right_half):
           
            merged_list = []
            left_index = right_index = 0
            
            while left_index < len(left_half) and right_index < len(right_half):
                if left_half[left_index] <= right_half[right_index]:
                    merged_list.append(left_half[left_index])
                    left_index += 1
                else:
                    merged_list.append(right_half[right_index])
                    right_index += 1
            
            merged_list.extend(left_half[left_index:])
            merged_list.extend(right_half[right_index:])
            
            return merged_list
        
        def solve(left, right, arr):
          
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            left_half = solve(left, mid, arr)
            right_half = solve(mid + 1, right, arr)
            
            return merge(left_half, right_half)
        
        return solve(0, len(nums) - 1, nums)