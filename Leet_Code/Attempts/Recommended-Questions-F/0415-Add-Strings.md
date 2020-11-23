# 415. Add Strings

Given two non-negative integers num1 and num2 represented as string, return the
sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.

---

Simple solution would be to converting the integers into number form, but this
is not allowed as well as have to deal with the overflow situations.

Then, we treat this problem as a adding two numbers represented within a linked
list. First, we reverse the strings to iterate so that we cna start from the
least significant value. Then, we maintain the carray as we iterate on the
given strings, adding two nums.

---

Java:

```java

class Solution {
    
    public String addStrings(String num1, String num2) {
        int i = num1.length() - 1;
        int j = num2.length() - 1;

        StringBuilder result = new StringBuilder();
        int carry = 0;

        while (i >= 0 || j >= 0 || carry > 0) {
            if (i >= 0) {
                carry += Integer.valueOf(num1.charAt(i) - '0');
                i--;
            }
            if (j >= 0) {
                carry += Integer.valueOf(num2.charAt(j) - '0');
                j--;
            }
            result.append(Integer.toString(carry % 10));
            carry /= 10;
        }

        return result.reverse().toString();
    }
}

```

Python:

```python

class Solution:
    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        result, carry = list(), 0
        while num1 or num2 or carry:
            if num1:
                carry += int(num1)
                num1 = num1[1:]
            if num2:
                carry += int(num2)
                num2 = num2[1:]
            result.append(str(carry % 10))
            carry //= 10
        return "".join(result[::-1])
```
