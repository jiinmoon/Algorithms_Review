# Largest Number

    Given a list of non negative integers, arrange them such that they form the
    largest number.

---

## Approach:

Think of this problem as a string concatenation problem; we sort the given
array in order such that concatenating two strings will produce larger
decending order of the list of strings.

Time complexity would be O(n * log(n)) due to sorting involved.

---

Java:

```java

public class Solution {

    public String largestNumber(final int[] A) 
    {
        String[] arr = new String[A.length];
        
        for (int i = 0; i < A.length; i++)
            arr[i] = String.valueOf(A[i]);
            
        Arrays.sort(arr, (a, b) -> {
            return (b + a).compareTo(a + b);
        });
        
        StringBuilder result = new StringBuilder();
        
        int i = 0;
        while (i < arr.length - 1 && arr[i].equals("0"))
            i++;
        
        while (i < arr.length)
            result.append(arr[i++]);
            
        return result.toString();
    }
    
}

```

Python:

```python

from functools import cmp_to_key

class Solution:

    def largestNumber(self, A):

        def helper(a, b):
            if a + b > b + a:
                return -1
            return 1
        
        A = list(map(str, A))

        A.sort(key = cmp_to_key(helper))

        while len(A) > 1 and A[0] == "0":
            A = A[1:]

        return "".join(A)
```
