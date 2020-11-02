# 273 Integer to English Words

Appending from right to left, we examine the given integer in every 1000. Map
the 10s, 100s. Be mindful of digits where every thousands we need to append the
(miilion, billion, etc...).

---

```python

class Solution:
    def integerToEnglish(self, num):
        integer_to_words = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
            7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven",
            12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
            16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }
        digit_to_words = {
            3: "Thousand", 6: "Million", 9: "Billion", 12: "Trillion",
            15: "Quadrillion", 18: "Quintillion", 21: "Sextillion",
            24: "Septillion", 27: "Octillion", 30: "Nonillion"
        }
        if num <= 20:
            return integer_to_words[num]

        res = list()
        digits = 0
        while num:
            num, thousand = divmod(num, 1000)
            hundred, ten = divmod(thousand, 100)

            if thousand and digit > 0:
                res.append(digit_to_words[digit])
            digit += 3

            if ten >= 20:
                if ten % 10:
                    res.append(integer_to_words[ten % 10])
                res.append(integer_to_words[10 * (ten // 10)])
            elif ten:
                res.append(integer_to_words[ten])

            if hundred:
                res.append("Hundred")
                res.append(integer_to_words[hundred])

        return "".join(res[::-1])
```
