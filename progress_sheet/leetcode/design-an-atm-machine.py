class ATM:

    def __init__(self):
        self.atm=dict()
        self.atm[500]=0
        self.atm[200]=0
        self.atm[100]=0
        self.atm[50]=0
        self.atm[20]=0

    def deposit(self, banknotesCount: List[int]) -> None:
        self.atm[500]+=banknotesCount[-1]
        self.atm[200]+=banknotesCount[-2]
        self.atm[100]+=banknotesCount[-3]
        self.atm[50]+=banknotesCount[-4]
        self.atm[20]+=banknotesCount[-5]
        

    def withdraw(self, amount: int) -> List[int]:
            ans = [0] * 5
            for i, notes in enumerate(self.atm):
                t = min(self.atm[notes], amount // notes)
                amount -= t * notes
                ans[5-i-1] = t     
            if amount: return [-1]
            for i, notes in enumerate(self.atm):
                self.atm[notes] -= ans[5-i-1]
            return ans
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)