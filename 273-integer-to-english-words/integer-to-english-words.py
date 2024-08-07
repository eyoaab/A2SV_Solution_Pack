class Solution:
    def numberToWords(self, num: int) -> str:
        store = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        
        bigs = {
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }
        
        def change(num):
            if num < 20:
                return store[num]
            elif num < 100:
                return store[num // 10 * 10] + ('' if num % 10 == 0 else ' ' + store[num % 10])
            elif num < 1000:
                return store[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' ' + change(num % 100))
            else:
                for value in sorted(bigs.keys(), reverse=True):
                    if num >= value:
                        return change(num // value) + ' ' + bigs[value] + ('' if num % value == 0 else ' ' + change(num % value))

        if num == 0:
            return 'Zero'
        return change(num).strip()
