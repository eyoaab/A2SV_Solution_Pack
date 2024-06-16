class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        visited = set()

        for i in range(len(hours)):
            for j in range(i + 1,len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    visited.add(i)
                    visited.add(j)

                    ans += 1
                    # break

        return ans             
                    
