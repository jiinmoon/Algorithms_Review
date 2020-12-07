# 273. Integer to English Words

Convert a non-negative integer num to its English words representation.

---

Python:

```python

from collections import deque

class Solution273:

    def __init__(self):

        self.intMap = {
            1 : "One", 2 : "Two", 3 : "Three", 4 : "Four",
            5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight",
            9 : "Nine", 10 : "Ten", 11 : "Eleven", 12 : "Twelve",
            13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen",
            16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen",
            19 : "Nineteen", 20 : "Twenty", 30 : "Thirty",
            40 : "Forty", 50 : "Fifty", 60 : "Sixty",
            70 : "Seventy", 80 : "Eighty", 90 : "Ninety"
        }
        
        self.digitMap = {
            3 : "Thousand",
            6 : "Million",
            9 : "Billion"
        }

    def numberToWords(self, num):

        if not num:
            return "Zero"

        result = deque()
        digit = 0

        while num:

            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if digit > 0 and thousand:
                result.appendleft(self.digitMap[digit])
            digit += 3

            if ten:
                if ten <= 20:
                    result.appendleft(self.intMap[ten])
                else:
                    if ten % 10:
                        result.appendleft(self.intMap[ten % 10])
                    result.appendleft(self.intMap[10 * (ten // 10)])

            if hundred:
                result.appendleft("{} Hundred".format(self.intMap[hundred]))

        return " ".join(result)

```
