class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        N = len(words[0])
        total_ = len(words)
        substring_length = N * total_
        word_count = Counter(words)
        answer = []

        for i in range(N):
            left = i
            right = i
            current_count = defaultdict(int)
            words_matched = 0

            while right + N <= len(s):
                word = s[right:right + N]
                right += N

                if word in word_count:
                    current_count[word] += 1
                    words_matched += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + N]
                        current_count[left_word] -= 1
                        words_matched -= 1
                        left += N

                    if words_matched == total_:
                        answer.append(left)
                else:
                    current_count.clear()
                    words_matched = 0
                    left = right

        return answer
