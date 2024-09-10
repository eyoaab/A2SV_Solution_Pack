class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        l = [] 
        l1 = []
        l2 = []
        for i in range(0,12):
            l.append(i*10)
        for i in l:
            if i>=purchaseAmount:
                l1.append(i)
            if i<=purchaseAmount:
                l2.append(i)
        if min(min(l1) - purchaseAmount,purchaseAmount - max(l2)) == min(l1) - purchaseAmount:
            return 100 - min(l1)
        else:
            return 100 - max(l2)