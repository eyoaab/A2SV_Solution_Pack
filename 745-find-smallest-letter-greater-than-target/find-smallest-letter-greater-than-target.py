class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0,len(letters) - 1
        best = ""

        if letters[-1] <= target:
            return letters[0]

        while left <= right:
           mid=(left + right) // 2

           cur = letters[mid]
           if cur > target:
               right = mid - 1
               best = cur
           else :
               left = mid + 1  
           
        return best         


