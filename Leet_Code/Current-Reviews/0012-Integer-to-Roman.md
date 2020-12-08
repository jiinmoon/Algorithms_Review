# 12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and
M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27 is
written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

---

To convert the given number into the roman numerals, we try to see from 1000 to
1, how many times that we can insert these digits. This would be O(n) in time
complexity.

---

Java:

```java

class Solution {
    
    private String[] romans;
    private int[] digits;
    
    public Solution() {
        this.romans = new String[] {
            "M", "CM", "D", "CD", 
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        };
        
        this.digits = new int[] {
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        };
    }
    
    public String intToRoman(int num) {
        
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < this.romans.length; i++)
        {
            if (num == 0) 
                break;

            String roman = this.romans[i];
            int digit = this.digits[i];
            int count = num / digit;
            num %= digit;

            while (count-- > 0)
                result.append(roman);
        }
        
        return result.toString();
    }
}

```
