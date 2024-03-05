from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(current, index):
            if len(current) == len(s):
                answer.append(current)
                return
            if s[index].isalpha():
              
                backtrack(current + s[index].upper(), index + 1)
                backtrack(current + s[index].lower(), index + 1)

            else:
                backtrack(current + s[index], index + 1)

        answer = []
        backtrack("", 0)
        return answer
