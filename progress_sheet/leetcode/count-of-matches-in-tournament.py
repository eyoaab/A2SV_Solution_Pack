class Solution:
    def numberOfMatches(self, n: int) -> int:
        self.answer=0
        def recur(num):
            if num<=1:
                return
            if num%2==0:
                self.answer+=num//2
                recur(num//2)
            else:
                self.answer+= num//2
                recur((num//2)+1)
        recur(n)
        return self.answer        


                 
        