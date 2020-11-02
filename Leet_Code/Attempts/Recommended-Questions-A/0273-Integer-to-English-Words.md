# 273. Integer to English Words

Convert a non-negative integer num to its English words representation.

---

To convert the given integer into English words, we first create a mapping
between each integer (0-20, 30, 40, 50, 60, 70, 80, 90) as well as the digits
(Thousand, Million, Billion, ...). Then, we use modulo operation to iterate on
the given num at every thousand digit (3 digits) to build on the English word
with mapping created.

---

Python:

```python

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
        
        result = collections.deque()
        digit = 0
        while num:
            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if not digit or thousand:
                result.appendleft(digitMap[digit])
            digit += 3
            
            if ten <= 20:
                result.appendleft(intMap[ten])
            else:
                if ten % 10:
                    result.appendleft(intMap[ten % 10])
                result.appendleft(intMap[10 * (ten // 10)])

            if hundred:
                result.appendleft("Hundred " + intMap[hundred])

        return " ".join(result)
```
