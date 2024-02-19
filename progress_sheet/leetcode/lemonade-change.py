class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total=0
        five=0
        ten=0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                ten+=1
                five-=1
                if five<0:
                    return False
            else:
                if ten==0:
                    if five<3:
                        return False
                    five-=3
                else:
                    ten-=1
                    if five==0:
                        return False        
                    five-=1
            if five<0 or ten<0: return False      
        return True                
        