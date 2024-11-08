class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        vowels = 'aeiou'
        store = defaultdict(lambda: 0)

        for i, char in enumerate(word):
            if char in vowels:
                store[char] += 1
                if i == 0 or word[i-1] not in vowels:
                    left = pivot = i
         
                while len(store) == 5 and all(store.values()):
                    store[word[pivot]] -= 1
                    pivot += 1
                result += (pivot - left)
            else:
                store.clear()
                left = pivot = i+1
        
        return result