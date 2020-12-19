# 6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows:

string convert(string s, int numRows);

---

Create rows or "buckets" as many as given number of rows. For each character we
add to the buckets that are matching row numbers. When we hit the top or
bottom, we reverse the order that we place the rows. We start to place them
from top to bottom, then bottom to top; repeat.

O(n) in time complexity as we are iterating on the given string once.

---

```java

class Solution {

    public String convert(String s, int numRows) 
    {
        if (numRows == 1)
            return s;
        
        StringBuilder[] result = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++)
            result[i] = new StringBuilder();
        
        int row = 0, direction = -1;
        
        for (char c : s.toCharArray())
        {
            result[row].append(c);
            if (row == 0 || row == numRows - 1)
                direction = direction * -1;
            row += direction;
        }
        
        StringBuilder zigzag = new StringBuilder();
        for (StringBuilder r : result)
            zigzag.append(r.toString());
        
        return zigzag.toString();
    }
}
```
