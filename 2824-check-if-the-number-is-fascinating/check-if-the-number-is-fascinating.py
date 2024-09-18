class Solution:
    def isFascinating(self, n: int) -> bool:
        store = str(n) + str(2 * n) + str(3 * n)

        if '0' in store:
            return False
        if len(store)>9:
            return False
        for i in range(1,10):
            if str(i) not in store :
                return False
        return True