# 48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

---

To rotate the given matrix, we can first reverse the matrix row-wise. Then,
swap the value diagonally. This is O(n) in time complexity without additional
space.

Think differently in terms of matrix transpose problem. First, we transpose the
matrix such that all values are swapped across diagonally. Then, we swap every
value column-wise on every row. This approach is inverse of above.

```
[1, 2, 3]               [1, 4, 7]           [7, 4, 1]
[4, 5, 6]   Transpose   [2, 5, 8]   Swap    [8, 5, 2]
[7, 8, 9]               [3, 6, 9]           [9, 6, 3]
```

---

Java: transpose; then swap (reverse each row).

```java

class Soluton { 

    public void rotateMatrix(int[][] matrix) {
        if (matrix.length == 0) return;

        int n = matrix.length;

        // 1. transpose
        for (int i = 0; i < n; i++) {
            for (int i = j + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // 2. reverse each row
        for (int[] m : matrix) {
            int i = 0;
            int j = n - 1;
            while (i < j) {
                int temp = m[i];
                m[i++] = m[j];
                m[j--] = temp;
            }
        }
    }
}

```

Java: reverse first then transpose.

```java

class Solution {

    public void rotateMatrix(int[][] matrix) {
        if (matrix.length == 0) return;

        int n = matrix.length;
        int i = 0;
        int j = n - 1;

        while (i < j) {
            int[] temp = matrix[i];
            matrix[i++] = matrix[j];
            matrix[j--] = temp;
        }

        for (i = 0; i < n - 1; i++) {
            for (j = i + 1; j < n - 1; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
}

```
