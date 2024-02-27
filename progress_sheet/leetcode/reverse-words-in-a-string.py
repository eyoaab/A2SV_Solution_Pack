class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        return " ".join(li[::-1])
        