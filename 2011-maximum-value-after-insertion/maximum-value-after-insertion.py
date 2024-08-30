class Solution:
    sys.set_int_max_str_digits(100000)
    def maxValue(self, n: str, x: int) -> str:
        if int(n) > 0:
            answer = ""
            i = 0

            while i< len(str(n)):
                if int(str(n)[i]) < x:
                    return str( n[:i] + str(x) + n[i:])

                i += 1    

            return n + str(x)    
        else:
            i = 1

            while i< len(str(n)):
                if int(str(n)[i]) > x:
                    return '-' + (str(n[1:i]) + str(x) + str(n[i:]))

                i += 1    

            return  n + str(x)     