class Solution:
    def isSumEqual(self, first_word, second_word, target_word):
        def helper(s):
            val = ''
            len_ = len(s)
            i = 0
            while (i < len_):
                c = s[i]
                val += str(ord(c) - ord('a'))
                i += 1
            
            return int(val)

        val_1 = helper(first_word)
        val_2 = helper(second_word)
        val_target = helper(target_word)

        return val_1 + val_2 == val_target