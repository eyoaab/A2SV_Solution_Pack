class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        temp=s+"00"
        ans=""
        while(i<len(s)):
            if(temp[i+2]=='#'):
                ans+=chr(96 + int(s[i:i+2]))
                i+=3
            else:
                ans+=chr(96 + int(s[i]))
                i+=1    
            
          
        return ans        


            


        