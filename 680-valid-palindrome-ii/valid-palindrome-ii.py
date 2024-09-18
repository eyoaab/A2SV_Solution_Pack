class Solution:
    # Helper function to check if a substring is a palindrome
    def checkPalindrome(self, s: str, l: int, r: int) -> bool:
    
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return (self.checkPalindrome(s, l + 1, r) or 
                        self.checkPalindrome(s, l, r - 1))
            l += 1
            r -= 1
        
        return True