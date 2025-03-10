class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        store = [{}, {}]
        for v in "aeiou":
            store[0][v] = 1
        
        response, currentK, vowels, extraLeft, left = 0, 0, 0, 0, 0

        for right, rightChar in enumerate(word):
            if rightChar in store[0]:
                store[1][rightChar] = store[1].get(rightChar, 0) + 1
                if store[1][rightChar] == 1:
                    vowels += 1
            else:
                currentK += 1

            while currentK > k:
                leftChar = word[left]
                if leftChar in store[0]:
                    store[1][leftChar] -= 1
                    if store[1][leftChar] == 0:
                        vowels -= 1
                else:
                    currentK -= 1
                left += 1
                extraLeft = 0

            while vowels == 5 and currentK == k and left < right and word[left] in store[0] and store[1][word[left]] > 1:
                extraLeft += 1
                store[1][word[left]] -= 1
                left += 1

            if currentK == k and vowels == 5:
                response += (1 + extraLeft)

        return response