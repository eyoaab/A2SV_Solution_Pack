class Solution:
    def splitString(self, s: str) -> bool:
        def helper(cur,i):
            if i==len(s):
                return True

            for j in range(i,len(s)):
                x = int(s[i:j+1])
               # print(x)
                if cur-1 == x and helper(x,j+1):
                    return True

            return False

        for i in range(len(s)-1):
            num = int(s[:i+1])
            #print("num=",num)
            if helper(num,i+1):
                return True

        return False                    
