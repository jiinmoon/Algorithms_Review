# 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

---

Simplest approach would be to convert the binary string into integer format,
then convert their sum back into the binary format.

---

Java:

```java

class Solution {
    
    // overflows when a and b are large
    // throws NumberFormatException when converting
    public String addBinary1(String a, String b) {
        long num1 = Long.valueOf(a, 2);
        long num2 = Long.valueOf(b, 2);
        return Long.toBinaryString(num1 + num2);
    }

    // accepted solution
    public String addBinary2(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0
        
        // every carry is power of two
        StringBuilder result = new StringBuilder();
        while (i >= 0 || j >= 0 || carry > 0) {
            if (i >= 0) carry += (a.charAt(i--) - '0');
            if (j >= 0) carry += (b.charAt(j--) - '0');

            result.append(carry % 2);
            carry /= 2;
        }

        return result.reverse().toString();
    }
}

```

Python:

```python

class Solution:
    def addBinary(self, a, b):
        result = int(a, 2) + int(b, 2)
        return bin(result)[2:] # discard "0b"
```
