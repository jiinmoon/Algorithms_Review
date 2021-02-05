# 348. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending
order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

---

As the rows and columns are sorted in ascending order, we know that our Kth
smallest element has to be within the first K rows. Then, we can create our
initial min-heap with the first elements from each rows upto Kth. For K steps,
we can examine our current minimum element from our min-heap which is guranteed
to be our minimum element that has been added to the heap so far. If there are
more steps to process, then we push unto our heap the value next to current
value. Alternatively, we could simply create min heap out of entire matrix
elements and remove from heap for k number of times.

Time complexity would be O(k * log(n)) as we have to repeat k number of heap
operations.

---

Java:

```java

class Solution348 {

    public int kthSmallest(int[][] matrix, int k)
    {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return -1;

        int m = matrix.length, n = matrix[0].length, result = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(matrix[a/n][a%n], matrix[b/n][b%n]));

        for (int row = 0; row < Math.min(k, m); row++)
            pq.offer(row * n);

        while (k-- > 0)
        {
            int result = pq.poll();
            if (result % n + 1 < n)
                pq.offer(result + 1);
        }

        return matrix[result/n][result%n];
    }
}

```
