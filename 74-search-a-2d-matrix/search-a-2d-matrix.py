class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_in_row(row,value):

            left = 0
            right = len(row) - 1

            while left <= right:
                mid = (left + right)// 2

                if row[mid] == value:
                    return True
                elif row[mid] > value:
                    right = mid - 1
                else:
                    left = mid + 1   

            return False

        right = len(matrix) - 1
        left = 0

        while left <= right:
            mid = (left + right)// 2
            row = matrix[mid]

            if row[-1] >= target and row[0] <= target:
                return find_in_row(row,target)

            elif row[-1] < target:
                left = mid + 1
            elif row[0] > target :
                right = mid - 1   

        return False        

                             
            
