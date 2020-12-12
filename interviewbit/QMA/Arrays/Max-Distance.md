# Max Distance

Given an array A of integers, find the maximum of j - i subjected to the
constraint of A[i] <= A[j].

---

### (1) Sort.

We record each of the element's position in the hashmap and sort the array.
Then, iterate on sorted array updating the maximum starting position for each
value. O(n * log(n)) for time complexity and O(n) for space complexity.

### (2) Create left mins and right maxs arrays.

We iterate on the given array from left to find the minimum elements that can
be found up to that i-th point; likewise, we iterate from right to find maximum
elements to be found from behind. By doing so, we can iterate from start of two
arrays and expand our using two pointers. If min value at left array is smaller
or equal to the max value at right array, this is a potential candidate; we
record the maximum difference. Since candidate has been found, we update by
moving maximum forward. Otherwise, left minimum is moved. O(n) in time
complexity and space complexity.

---

Java:

```java

public class Solution {

    public int maximumGap(final List<Integer> A)
    {
        int m = A.size();
        int[] left_mins = new int[m];
        int[] right_maxs = new int[m];

        left_mins[0] = A.get(0);

        for (int i = 0; i < m; i++)
            left_mins[i] = Math.min(left_mins[i-1], A.get(i));

        right_maxs[m - 1] = A.get(m - 1);
        for (int i = m - 2; i >= 0; i--)
            right_maxs[i] = Math.max(right_maxs[i], A.get(i));

        int i = 0, j = 0, result = 0;

        while (i < m && j < n)
        {
            // so long as we can expand maximum, expand
            if (left_mins[i] <= right_maxs[j]) {
                result = Math.max(result, j - i);
                j++;
            } else {
            // otherwise, we move our starting position and try again
                i++;
            }
        }

        return result;
    }
}

```
