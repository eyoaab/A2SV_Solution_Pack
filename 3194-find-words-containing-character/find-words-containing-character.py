class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer  = [index for index,word in enumerate(words) if x in word]
        return answer
        