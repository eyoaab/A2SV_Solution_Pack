class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        
        for i in range(0, n, k):
            temp_sum = 0
            
            for j in range(i, min(i + k, n)):
                temp_sum += ord(s[j]) - ord('a')

            temp_sum = (temp_sum % 26) + ord('a')
            result.append(chr(temp_sum))
        
        return ''.join(result)
