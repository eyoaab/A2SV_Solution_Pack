class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)
            current = self.get_next_number(current, n)

        return result

    def get_next_number(self, current: int, n: int) -> int:
        if current * 10 <= n:
            return current * 10 

        if current >= n:
            current //= 10 

        current += 1  
        
        while current % 10 == 0:
            current //= 10 

        return current
        