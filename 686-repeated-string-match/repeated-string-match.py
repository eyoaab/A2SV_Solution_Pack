class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not set(b).issubset(set(a)):
            return -1
        
        repeat_count = ceil(len(b) / len(a))  
     
        repeated_a = a * repeat_count
        if b in repeated_a:
            return repeat_count
        elif b in repeated_a + a:
            return repeat_count + 1
        
        return -1
