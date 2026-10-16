class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        bit1 = [0] * (n + 1)
        bit2 = [0] * (n + 1)
        last = [-1] * 100001

        def prefix_sum(k: int) -> int:
            s1 = s2 = 0
            index = k
            while index > 0:
                s1 += bit1[index]
                s2 += bit2[index]
                index -= index & -index
            return k * s1 - s2

        def add_boundary(index: int, delta: int) -> None:
            weighted = delta * (index - 1)
            while index <= n:
                bit1[index] += delta
                bit2[index] += weighted
                index += index & -index

        total_distinct = 0
        ending_squares = 0
        answer = 0

        for i, value in enumerate(nums):
            p = last[value]
            
            affected_sum = total_distinct - prefix_sum(p + 1)
            length = i - p
            ending_squares = (ending_squares + 2 * affected_sum + length) % MOD
            answer = (answer + ending_squares) % MOD

            add_boundary(p + 2, 1)
            add_boundary(i + 2, -1)
            total_distinct += length
            last[value] = i

        return answer