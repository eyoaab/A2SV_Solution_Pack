class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        for word in words:
            flag = set(word) - set(allowed)
            if len(flag) == 0:
                answer += 1

        return answer        
        