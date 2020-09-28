# 273 Interger to English Words

Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 2^31 - 1.

---

We first create a mapping for all digits (thousands, million, billion...) and
integers between 1 to 90.

Then, we can use modulo operations to isolate the given integer at every
thousands - and thousands are isolated further into hundreds, and tens.

First, if tens exist, and it is greater than 20, then we need to take care of
the case of the single digits (i.e. integer less than 20 has a unique english
words such as 17 "seventeen" as compared to 27 "twenty seven"), then at tens.
Otherwise, we can simply add english word map of the tens.

Then, at hundreds, if it exist, it will be a simple mapping + the word,
"hundred".

While doing so, we also need to keep track of the number of digits - since we
are looking at every thounsands, we maintain the digits at interval of 3, 6,
9...and so on.

---

Python:

```python
from collections import deque

class Solution:
    def numberToWords(self, num):
        intMap = {
            1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
            6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
            11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
            15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
            19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty',
            50 : 'Fifty', 60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty',
            90 : 'Ninety'
        }
        digitMap = {
            3 : 'Thousand', 6  : 'Million', 9 : 'Billion', 12 : 'Trillion',
            15 : 'Quadrillion', 18 : 'Quintillion', 21 : 'Sextillion',
            '24' : 'Septillion', 27 : 'Octillion', 30 : 'Nonillion'
        }
	
	result = deque()
        digits = 0

        if num == 0:
            return "Zero"

        while num:
            num, thousands = divmod(num, 1000)
            hundreds, tens = divmod(num, 100)

            if thousands and digits > 0:
                result.appendleft(digitMap[digits])
            digits += 3

            if tens >= 20:
                if tens % 10:
                    result.appendleft(intMap[tens % 10])
                result.appendleft(intMap[10 * (tens // 10]))
            elif tens:
                result.appendleft(intMap[tens])

            if hundreds:
                result.appendleft("hundred")
                result.appendleft(intMap[hundreds])

        return " ".join(result)
```
