class Solution:
    def isPalindrome(self, s: str) -> bool:
        def rem(string):
            sk = re.sub(r'\W+', '', string)
            return sk
        s= rem(s)   
        s=s.replace(',','')
        s=s.replace('.','')
        s=s.replace('!','')
        s=s.replace('?','')
        s=s.replace(':','')
        s=s.replace(';','')
        s=s.replace('"','')
        s=s.replace('\'','')
        s=s.replace(' ','')
        s=s.replace('@','')
        s=s.replace('_','')


        s=s.lower()
        l=0
        r=len(s)-1
        while(l!=r and r>l):
            if(s[l]!=s[r]):
                return False
            else:
                l=l+1
                r=r-1        
        return True