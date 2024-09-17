class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list_one = s1.split()
        list_two = s2.split()
        count = 0
        answer = []

        for i in list_one:
            if i not in list_two and list_one.count(i) == 1:
                answer.append(i)
        for i in list_two:
            if i not in list_one and list_two.count(i)==1:
                answer.append(i)
                
        return answer

        