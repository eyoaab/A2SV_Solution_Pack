class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        pos = [0] * n
        for i, val in enumerate(nums2):
            pos[val] = i

        store = [pos[val] for val in nums1]

        def update(bit, idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx

        def query(bit, idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        left = [0] * n
        bit = [0] * (n + 2)  

        for i in range(n):
            left[i] = query(bit, store[i])
            update(bit, store[i] + 1, 1)  

        right = [0] * n
        bit = [0] * (n + 2)

        for i in reversed(range(n)):
            right[i] = query(bit, n) - query(bit, store[i] + 1)
            update(bit, store[i] + 1, 1)

        return sum(left[i] * right[i] for i in range(n))