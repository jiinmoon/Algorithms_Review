# 36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily
solvable.

Only the filled cells need to be validated according to the mentioned rules.

---

To determine whether the given board in valid, we do not have to solve it, but
only check that each rows, columns, and boxes does not contain any duplicates.

We may use a list or set to check for duplicate items; but we can save space by
using `int` as the given values must be within values 1-9. Hence, all the
values can occupfy within the size of `int`. This can be checked with bit-wise
operation AND (&).

Time complexity would be O(m * n) and space complexity would be O(n).

---

Java:

```java

class Solution36 {

    public boolean isValidSudoku(char[][] board)
    {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int r = 0; r < 9; r++)
        {
            for (int c = 0; c < 9; c++)
            {
                int curr = 1 << (board[r][c] - '0');
                int b = (r / 3) * 3 + (c / 3);

                if (rows[r] & curr != 0 || cols[c] & curr != 0 || boxes[b] & curr != 0)
                    return false;
                
                rows[r] |= curr;
                cols[c] |= curr;
                boxes[b] |= curr;
            }
        }
        
        return true;
    }
}

```
