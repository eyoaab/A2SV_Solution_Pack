class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        li=[]
        for i in range(len(prices)):
            fl=True
            for j in (prices[i+1:]):
                if(prices[i]>=j):
                    li.append(abs(prices[i]-j))
                    fl=False
                    break
            if(fl):
                li.append(prices[i])      
        return li
        