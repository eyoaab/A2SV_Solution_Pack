class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return str(0)
        
        ans = []
        
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)

        first = numerator // denominator
        ans.append(str(first))

        remainder =  numerator % denominator
        if remainder == 0:
            return "".join(ans)
        
        ans.append(".")

        hm = {}

        while remainder != 0:
            if remainder in hm:
                ans.insert(hm[remainder], "(")
                ans.append(")")
                return "".join(ans)
            
            hm[remainder] = len(ans)

            remainder *= 10
            digit = remainder // denominator
            ans.append(str(digit))
            remainder %= denominator
        
        return "".join(ans)