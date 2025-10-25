class Solution:
    def totalMoney(self, n: int) -> int:
        i = 1
        j = 1
        money = 0
        days = 1

        while j <= n:
            money += i
            i += 1
            j += 1
            if i == days + 7:
                days += 1
                i = days

        return money         

        