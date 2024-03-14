class Bitset:

    def __init__(self, size: int):
        self.bitsSet_0 = ['0'] * size
        self.bitsSet_1 = ['1'] * size
        self.ans=0
        self.ans2=size

    def fix(self, idx: int) -> None:
        if self.bitsSet_0[idx] == '0': 
            self.bitsSet_0[idx] = '1'
            self.ans+=1
            self.bitsSet_1[idx] = '0'
            self.ans2-=1

    def unfix(self, idx: int) -> None:
        if self.bitsSet_0[idx] == '1': 
            self.bitsSet_0[idx] = '0'
            self.ans-=1
            self.bitsSet_1[idx] = '1'
            self.ans2+=1

    def flip(self) -> None:
        self.bitsSet_0,self.bitsSet_1=self.bitsSet_1,self.bitsSet_0
        self.ans2,self.ans=self.ans,self.ans2
       
        
    def all(self) -> bool:
        return self.ans == len(self.bitsSet_0)

    def one(self) -> bool:
        return self.ans>0

    def count(self) -> int:
        return self.ans

    def toString(self) -> str:
        return ''.join(self.bitsSet_0)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
