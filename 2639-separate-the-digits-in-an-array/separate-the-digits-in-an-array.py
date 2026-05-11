class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        def todigit(num):
            ans = []
            for n in str(num):
                ans.append(int(n))

            return ans

        for num in nums:
            answer.extend(todigit(num))

        return answer              