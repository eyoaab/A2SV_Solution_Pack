class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        pref = [0]
        for x in nums:
            pref.append(pref[-1] + (1 if x == target else -1))

        values = sorted(set(pref))

        bit = [0] * (len(values) + 2)

        def update(idx):
            while idx < len(bit):
                bit[idx] += 1
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        ans = 0

        for x in pref:

            idx = bisect_left(values, x) + 1

            ans += query(idx - 1)

            update(idx)

        return ans