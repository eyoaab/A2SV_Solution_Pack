class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lpm = [0 for i in range(len(needle))]

        i,j = 0,1

        while j < len(needle):
            if needle[i] == needle[j]:
                lpm[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lpm[i - 1]  

        i,j = 0, 0  

        while i < len(needle) and j < len(haystack):
            if needle[i] ==  haystack[j]:
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lpm[i - 1] 

            if i == len(needle):
                return j - i

        return -1                                      