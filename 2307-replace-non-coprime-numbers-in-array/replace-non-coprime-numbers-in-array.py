def llcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                num = llcm(stack.pop(), num)
            stack.append(num)

        return stack
