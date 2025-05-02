class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        A = ['L', *dominoes, 'R']
        n = len(A)
        prev = 0

        for i in range(1, n):
            cur = A[i]
            if cur == '.':
                continue

            prev_val = A[prev]
            gap = i - prev - 1

            if prev_val == cur:
                if gap:
                    A[prev + 1:i] = [cur] * gap
            elif prev_val == 'R':
                half = gap // 2
                if half:
                    A[prev + 1:prev + 1 + half] = ['R'] * half
                    A[i - half:i] = ['L'] * half

            prev = i

        
        return ''.join(A[1:-1])