class Solution:
    MAX = 100005
    pref = [0] * MAX
    
    for i in range(100, MAX):
        snum = str(i)
        waviness = 0
        
        for j in range(1, len(snum) - 1):
            if (snum[j] < snum[j - 1] and snum[j] < snum[j + 1]) or \
               (snum[j] > snum[j - 1] and snum[j] > snum[j + 1]):
                waviness += 1
        pref[i] = pref[i - 1] + waviness

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.pref[num2] - self.pref[num1 - 1]