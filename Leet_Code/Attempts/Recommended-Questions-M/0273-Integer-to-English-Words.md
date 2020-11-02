# 273 Integer to English Words

Convert a non-negative integer num to its English words representation.

---

To convert the given positive integer to english words, we first create
a hashmap mapping of the integer and digits to its English word counterparts.
Then, we iterate on the given num using the modulo operation to go through at
every 3 digits at a time. We identify the thousand, hundred and tens. Then, we
can append their English counterparts to the result to be returned. Overall,
the time complexity would simply be O(n) where n is the size of the integer.

---

Python:

```python

class Solution:
    def integerToEnglishWords(self, num):
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
        
        # as we are iterating on the given num from right to left,
        # build the words same way.
        result = collections.deque()
        digit = 0

        while num:
            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(num, 100)

            if not digit and thousand:
                result.appendleft(digitmap[digit])
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

