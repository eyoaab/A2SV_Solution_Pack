class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        store = {}
        index = 0
        right = "abcdefghijklmnopqrstuvwxyz"
        for i,char in enumerate(key):
            if char not in store and char != ' ':
                # print(index)
                store[char] = right[index]
                index += 1

        ans = ""
        for word in message:
            if word == " ":
                ans += " "
            else:    
                ans += store[word]
                 

        return ans         