class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {} 
        self.timeToLive = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
       
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        x=0
        for i,j in self.tokens.items():
            if j > currentTime:
                x+=1
        return x    
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId, currentTime)
# obj.renew(tokenId, currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
