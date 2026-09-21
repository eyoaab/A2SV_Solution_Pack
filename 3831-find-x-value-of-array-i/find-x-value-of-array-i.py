class Solution:
    def resultArray(self, A: List[int], k: int) -> List[int]:
        res = [0] * k
        freq = [0] * k

        for n in A:
            n %= k
            cur = [0] * k
            cur[n] = 1

            for x, c in enumerate(freq):
                cur[x * n % k] += c

            freq = cur
            for x, c in enumerate(freq):
                res[x] += c

        return res