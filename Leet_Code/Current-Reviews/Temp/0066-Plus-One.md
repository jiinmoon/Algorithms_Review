# 66. Plus One

Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

---

We carry over so long as current digit is 9. If curr digit is 9, then it should
be set to 0. First non-nine digit should be incremented plus one. If all are
nines, then we have to resize the array. O(n) in time complexity where n is the
number of digits to process.

---

Java:

```java

class Solution66 {

    public int[] plusOne(int[] digits) 
    {
        for (int i = digits.length-1; i >= 0; i--)
        {
            if (digits[i] == 9){
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }
        
        int[] result = new int[digits.length+1];
        result[0] = 1;
        return result;
    }
}

```
