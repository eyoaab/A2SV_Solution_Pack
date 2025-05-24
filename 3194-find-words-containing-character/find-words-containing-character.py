class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []

        for index,word in enumerate(words):
            if x in word:
                answer.append(index)

        return answer        