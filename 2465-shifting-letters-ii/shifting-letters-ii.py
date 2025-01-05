class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        prefix = [0 for i in range( N + 1)]

        for start,end,direction in shifts:

            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1

            else:
                prefix[start] -= 1
                prefix[end + 1]  += 1 

        for i in range(1,N + 1):
            prefix[i] = prefix[i] +  prefix[i - 1] 

        a = ord('a')
        result = []

        for idx,ch in enumerate(s):
            change = (ord(ch) - a + prefix[idx] ) % 26
            result.append(chr(change + a))

        return ''.join(result)                
