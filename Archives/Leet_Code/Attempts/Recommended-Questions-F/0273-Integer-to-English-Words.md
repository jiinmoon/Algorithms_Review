# 273. Integer to Enlgish Words

Convert a non-negative integer num to its English words representation.

---

First, we create a mapping for integer as well as digit to its English words.
Then, from given num, we iterate on every 3 digits (thousands) to extract
hundred-th and ten-th to append their English mapping to result. Note that
under integer 20, there are respective English words - thus, we can append as
is. But over 20, we also need to take care of the single digit case as well as
ten-th digit. The time complexity would be O(log n) where n is the size of the
given number since we are reducing the size of the given number logrithmically
at each iteration.

---

Python:

```python

class Solution:
    def numToWords(self, num):
        intMap = {
            1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
            6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
            11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
            15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
            19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty',
            50 : 'Fifty', 60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty',
            90 : 'Ninety', 0 : 'Zero'
        }
        digitMap = {
            3 : 'Thousand', 6  : 'Million', 9 : 'Billion', 12 : 'Trillion',
            15 : 'Quadrillion', 18 : 'Quintillion', 21 : 'Sextillion',
            '24' : 'Septillion', 27 : 'Octillion', 30 : 'Nonillion'
        }

        digit = 0
        # since we are looking at the elements from behind
        # build the words from right to left
        result = collections.deque()
        while num:
            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if not digit or thousand:
                result.appendleft(digitMap[digit])
            digit += 3

            if ten <= 20:
                result.appendleft(intMap[ten])
            else:
                # last digit
                if ten % 10:
                    result.appendleft(intMap[ten % 10])
                result.appendleft(intMap[10 * (ten // 10)])

            if hundred:
                result.appendleft("Hundred {}".format(intMap[hundred]))

        return " ".join(result)
```
