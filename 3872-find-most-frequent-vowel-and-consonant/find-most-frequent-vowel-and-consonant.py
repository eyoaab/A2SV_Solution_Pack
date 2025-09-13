class Solution:
    def maxFreqSum(self, s: str) -> int:
        values = defaultdict(int)
        consonents = defaultdict(int)
        vaul = 'aeiou'
        maxVal = 0
        maxCons = 0

        for letter in s:
            if letter in vaul:
                values[letter] += 1
                maxVal = max(maxVal, values[letter])
            else:
                consonents[letter] += 1    
                maxCons = max(maxCons, consonents[letter])


        return maxVal + maxCons