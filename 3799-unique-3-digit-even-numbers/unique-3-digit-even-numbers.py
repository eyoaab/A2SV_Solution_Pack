class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = [0] * 10
        for d in digits:
            digit_counts[d] += 1
            
        ans = 0
        
        for num in range(100, 1000, 2):
            a = num // 100
            b = (num // 10) % 10
            c = num % 10
            
            digit_counts[a] -= 1
            digit_counts[b] -= 1
            digit_counts[c] -= 1
            
            if digit_counts[a] >= 0 and digit_counts[b] >= 0 and digit_counts[c] >= 0:
                ans += 1
                
            digit_counts[a] += 1
            digit_counts[b] += 1
            digit_counts[c] += 1
            
        return ans