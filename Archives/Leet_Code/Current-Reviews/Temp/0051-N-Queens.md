# 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space,
respectively.

---

We can use recursive backtracking algorithm to generate all possible solutions
to the N-Queens. By going through row after row, we can place a queen on any of
the n tiles. Then, all we have to maintain is that previous information about
where the queens were placed to avoid placing the queen in the invalid space.

O(n!) time complexity due to exhaustively cnosidering every position. O(n) in
space to maintain the states of the board and paths.

---

Java:

```java

class Solution51 {
    
    private int n;
    private List<List<String>> result;
    private boolean[] cols, ups, downs;
    
    public List<List<String>> solveNQueens(int n) {
        
        this.n = n;
        this.result = new ArrayList<>();
        // marks the positions of the placed queens
        this.cols = new boolean[n];
        // there are two diagonal lines:
        // (1) Up-diagonal: (row - col)
        // (2) Down-diagonal: (row + col)
        this.ups = new boolean[2 * n - 1];
        this.downs = new boolean[2 * n - 1];
        
        char[][] path = new char[n][n];
        for (int i = 0; i < n; i++)
        {
            char[] temp = new char[n];
            Arrays.fill(temp, '.');
            path[i] = temp;
        }
        
        backtrack(0, path);
        
        return result;
    }
    
    private void backtrack(int row, char[][] path)
    {
        // end of backtrack
        if (row == this.n) {

            List<String> temp = new ArrayList<>();
            for (char[] r : path)
            {
                String s = String.valueOf(r);
                temp.add(s);
            }
            this.result.add(temp);

        } else {

            for (int col = 0; col < this.n; col++)
            {
                // is current cell valid?
                // row - col ranges (-n, +n)
                if (this.cols[col] || this.ups[row + col] || this.downs[row - col + n - 1])
                    continue;
                
                // place queen
                path[row][col] = 'Q';
                this.cols[col] = true;
                this.ups[row + col] = true;
                this.downs[row - col + n - 1] = true;

                backtrack(row + 1, path);

                // restore for next case
                this.downs[row - col + n - 1] = false;
                this.ups[row + col] = false;
                this.cols[col] = false;;
                path[row][col] = '.';
            }
        }
    }
}

```
