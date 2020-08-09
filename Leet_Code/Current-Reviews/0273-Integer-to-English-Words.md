273 Integer to English Words
============================

Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 2^31 - 1.

Example 1:

```
Input: 123
Output: "One Hundred Twenty Three"
```

Example 2:

```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

Example 3:

```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

Example 4:

```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
Thousand Eight Hundred Ninety One"
```

---

We will simply group the words in 3 digits, and use hashmap to map our numbers
into the words. We will need to create a long mapping since there are 20
distinct mappings between int 1 - 20, and every 10 increments to 90. Also, we
need to keep track of number of digits as well. i.e. 3 digits imply it is
'Thousand', 6 means 'Million', and so on.

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
            19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Fourty',
            50 : 'Fifty', 60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty',
            90 : 'Ninety'
        }
        digitMap = {
            3 : 'Thousand', 6  : 'Million', 9 : 'Billion', 12 : 'Trillion',
            15 : 'Quadrillion', 18 : 'Quintillion', 21 : 'Sextillion',
            '24' : 'Septillion', 27 : 'Octillion', 30 : 'Nonillion'
        }
        words = deque()
        digits = 0
        if num == 0:
            return "Zero"
        while num:
            num, section = divmod(num, 1000)
            hundreds, tens = divmod(section, 100)

            if section and digits > 0:
                words.appendleft(digitMap[digits])
            digits += 3

            if tens >= 20:
                if tens % 10:
                    words.appendleft(intMap[tens%10])
                words.appendleft(intMap[10*(tens//10)])
            elif tens:
                words.appendleft(intMap[tens])

            if hundreds:
                words.appendleft("Hundred")
                words.appendleft(intMap[hundreds])
        return " ".join(words)
```
