class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i][0] != sentence[i-1][-1]:
                return False

        return True        