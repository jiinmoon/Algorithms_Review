# 273 Integer to English Words
#
# Use modulous operation to isolate the every 1000, and 100, 10 digits from
# "right to left". 
#
# Since we are examining each section in 1000, we keep track of current digits
# to determine 'Thousands' to 'Nonillion' (from 3 to 30) to append to our
# result.
#
# Then, we take a look at sections of 10s and 100s, and map them appropriately
# to its english words.

class Solution:
    def numberToWords(self, num):
        integer_words = {
            0 : "Zero", 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four",
            5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 
            10 : "Ten", 11 : "Eleven", 12 : "Twelve", 13 : "Thirteen",
            14 : "Fourteen", 15 : "Fifteen", 16 : "Sixteen", 17 : "Seventeen",
            18 : "Eighteen", 19 : "Nineteen", 20 : "Twenty", 30 : "Thirty",
            40 : "Forty", 50 : "Fifty", 60 : "Sixty", 70 : "Seventy",
            80 : "Eighty", 90 : "Ninety"
        }

        digit_words = {
            3 : "Thousands", 6 : "Million", 9 : "Billion", 12 : "Trillion",
            15 : "Quadrillion", 18 : "Quintillion", 21 : "Sextillion",
            24: "Septillion", 27 : "Octillion", 30 : "Nonillion"
        }

        if num in integer_words:
            return integer_words[num]

        res = collections.deque()
        digits = 0

        while num:
            # i.e. divmod(1331, 1000) will yield 1, 331
            num, thousands = divmod(num, 1000)
            hundreds, tens = divmod(thousands, 100)

            if tousands and digits > 0:
                res.appendleft(digit_words[digits])
            digits += 3
            
            if tens >= 20:
                # take care of single digit
                if tens % 10:
                    res.appendleft(integer_words[tens % 10])
                res.appendleft(integer_words[(tens // 10) * 10])
            elif tens:
                res.appendleft(integer_words[tens])

            if hundreds:
                res.appendleft("Hundred")
                res.appendleft(integer_words[hundreds])

        return " ".join(res)

