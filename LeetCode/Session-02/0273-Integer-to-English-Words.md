# 273. Integer to English Words

Convert a non-negative integer num to its English words representation.

---

This is a mapping problem where we divide the given integer into digits that we
can digest and map unto English equivalent. There are numerous edge cases to
consider such as there is one-to-one mapping between 1-19, and so on.

Hence, we would consider every thousand digits for given integer using moduolo
operation as we have to append digit modifier ("Billion" and so on).

---

Python:

```python

class Solution273:

    def intToWord(self, num):

        if not num:
            return "Zero"

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

        result = deque()
        digit = 0

        while num:

            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if digit > 0 and thousand:
                result.appendleft(self.digitMap[digit])
            digit += 3

            if ten:
                # ten-th digit between 1 - 20 has one-to-one map
                if ten <= 20:
                    result.appendleft(self.intMap[ten])
                # otherwise, append first digit followed by next
                else:
                    if ten % 10:
                        result.appendleft(self.intMap[ten % 10])
                    result.appendleft(self.intMap[10 * (ten // 10)])

            if hundred:
                result.appendleft(self.intMap[hundred] + " Hundred")

        return " ".join(result)
```

