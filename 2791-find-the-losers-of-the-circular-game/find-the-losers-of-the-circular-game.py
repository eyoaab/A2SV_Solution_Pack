class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        friends = [False for i in range(n)]
        index = 0
        count = 1
        while not friends[index]:
            friends[index] = True

            index += ((count * k) + n) % n
            count += 1
            index %= n



        return [i + 1 for i,j in enumerate(friends) if not j]
        