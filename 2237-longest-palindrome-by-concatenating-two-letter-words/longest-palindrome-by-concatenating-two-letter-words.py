class Solution(object):
    def longestPalindrome(self, words):
        store = [[0] * 26 for _ in range(26)]
        ans = 0
        middle = 0

        for word in words:
            x, y = ord(word[0]) - ord('a'), ord(word[1]) - ord('a')
            if store[y][x] > 0:
                store[y][x] -= 1
                ans += 4
                if x == y:
                    middle -= 1
            else:
                store[x][y] += 1
                if x == y:
                    middle += 1

        if middle > 0:
            ans += 2

        return ans