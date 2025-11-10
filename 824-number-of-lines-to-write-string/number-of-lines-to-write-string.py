class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total = 1
        curr = 0
        
        for char in s:
            index = ord(char) - ord('a')  
            char = widths[index]     
            
            if curr + char > 100:
                total += 1     
                curr = char  
            else:
                curr += char  
        
        return [total, curr]

   