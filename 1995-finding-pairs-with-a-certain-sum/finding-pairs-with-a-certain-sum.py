class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.n1 = nums1
        self.n2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        old = self.n2[index]
        self.freq[old] -= 1
        self.n2[index] += val
        self.freq[self.n2[index]] += 1

    def count(self, tot):
        res = 0
        for x in self.n1:
            res += self.freq[tot - x]
        return res