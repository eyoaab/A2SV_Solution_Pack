class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        answer = 0
        
        for left in range(n):
            vowel_count = defaultdict(int)
            consonant_count = 0
            unique_vowels = 0  

            for right in range(left, n):
                c = word[right]
                if c in vowels:
                    if vowel_count[c] == 0:
                        unique_vowels += 1
                    vowel_count[c] += 1
                else:
                    consonant_count += 1

              
                if consonant_count > k:
                    break

                if unique_vowels == 5 and consonant_count == k:
                    answer += 1

        return answer