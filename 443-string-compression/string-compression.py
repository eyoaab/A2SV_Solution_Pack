class Solution(object):
    def compress(self, chars):
        n = len(chars)
        if n == 1:
            return 1
        
        i = 0
        j = 0
        
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
            i += 1
        
        return j