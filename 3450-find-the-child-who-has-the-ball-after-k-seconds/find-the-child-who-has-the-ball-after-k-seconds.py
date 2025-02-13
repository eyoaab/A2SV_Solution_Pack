class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        index = 0
        isFor = True
        while k:
            k -= 1
            if isFor:
                index += 1
            else:
                index -= 1

            if index == 0 or index == n - 1:
                isFor = not isFor                
        return index
        