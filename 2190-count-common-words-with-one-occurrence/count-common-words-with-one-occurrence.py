class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        store1 = Counter(words1)
        store2 = Counter(words2)

        answer = 0

        for word in words1:
            if store1[word] == 1 and store2[word] == 1:
                answer += 1

        return answer       

        
