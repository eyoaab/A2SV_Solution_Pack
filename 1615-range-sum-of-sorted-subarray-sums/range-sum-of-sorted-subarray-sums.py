class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ref = []
        for i in range(len(nums)):
            _sum = 0
            for j in range(i,len(nums)):
                _sum += nums[j]
                ref.append(_sum)
        ref.sort()
        pre=[0]
        # print(ref)
        for num in ref:
            pre.append(pre[-1]+num)
        return pre[right]%(1000000007)-pre[left-1]%(1000000007)   