class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 1
        last_added = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            
            added = (total - last_added[idx]) % MOD
            total = (total + added) % MOD
            last_added[idx] = (last_added[idx] + added) % MOD
            
        return (total - 1) % MOD