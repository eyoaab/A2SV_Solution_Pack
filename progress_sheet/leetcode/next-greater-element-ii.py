class Solution:
        def nextGreaterElements(self, A):
            stack, res = [], [-1] * len(A)
            for i in range(len(A) * 2):
                while stack and (A[stack[-1]] < A[i%len(A)]):
                    res[stack.pop()] = A[i%len(A)]
                stack.append(i%len(A))
            return res  
        