# Next Permutation

Implement the next permutation, which rearranges numbers into the numerically
next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest
possible order i.e., sorted in an ascending order.

---

Realize that complete reversed sorted integer such as [ 4, 3, 2, 1 ] has a next
permutation that is in reverse which is [ 1, 2, 3, 4 ]. Hence, we can find from
behind the first out of place element, then swap this with greater value
encountered; and reverse the segment.

For example, in [ 0, 3, 4, 2, 1 ] first out of place element from behind is 3.
Then, we swap it with next greater element which is 4 and reverse the segement
where out of place element was found + 1.

[ 0, 3, 4, 2, 1 ]   <-- 3 is out of place.
[ 0, 4, 3, 2, 1 ]   <-- search from behind; 4 is next greater; swap.
[ 0, 4, 1, 2, 3 ]   <-- reverse from i = 2; next permutation found.

O(n) in time complexity.

---

Java:

```java

public class Solution {

    public ArrayList<Integer> nextPermutation(ArrayList<Integer> A) 
    {
        int m = A.size();
        int i = m - 2, j = m - 1;
        
        for (; i >= 0 && A.get(i+1) <= A.get(i); i--);
        
        if (i >= 0)
        {
            for (; j > i && A.get(j) <= A.get(i); j--);

            int temp = A.get(i);
            A.set(i, A.get(j));
            A.set(j, temp);
        }
        
        int l = i + 1, r = m - 1;
        while (l < r)
        {
            int temp = A.get(l);
            A.set(l, A.get(r));
            A.set(r, temp);
            l++; r--;
        }
        
        return A;
    }
}

```
