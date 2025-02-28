class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        gcd_length = gcd(len1, len2)
        
        candidate = str1[:gcd_length]
        
        if candidate * (len1 // gcd_length) == str1 and candidate * (len2 // gcd_length) == str2:
            return candidate
        else:
            return ""


  