class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1],[1,1]]

        answer = [[1],[1,1]]

        for _ in range(numRows - 2):
            dp = answer[-1][:]
            
            for i in range(len(dp) - 1):
                dp[i] = dp[i] + dp[i + 1]

            # trmp =  [1]  +temp + [1] 
            dp = [1] + dp  
            answer.append(dp)

        return answer          
                