class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = ['1','2','3','4','5','6','7','8','9']
        minWindow = len(str(low))
        maxWindow = len(str(high))
        window = minWindow
        out = []
        ctr = 0
        while window <= maxWindow:
            if ctr == 0:
                start = int(str(low)[0]) - 1
            else:
                start = 0
            for i in range(start, len(digits)):
                num = ''
                if(i+window > len(digits)):
                    break
                for j in range(i, i+window):
                    num += digits[j]
                if(int(num) < low):
                    continue
                else:
                    if(int(num) <= high):
                        out.append(int(num))
                    else:
                        break
            ctr += 1
            window += 1
        return out

        