class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        c = False
        
        for i in range(len(num)):

            a = int(num[i])
            if change[a] > a:
                num[i] = str(change[a])
                c = True
            elif change[a] == a and c:
                continue
            elif c:
                break

        return "".join(num)