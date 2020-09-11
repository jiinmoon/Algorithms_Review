79 Word Searech
===============

Given a 2D board and a word, find if the word exists in the grid.

---

This is a typical backtracking algorithm - searching for the matching
characters in four directions.

---

C++:

Notice the neat usage of the `const_iterator`; passing the entire string of
word is magnitudes slower. Utilize references and pointers to avoid unnecessary
computations and copying of values.

```cpp
# type alias
using s_iter = string::const_iterator;

class Solution {
public:
    bool explore(vector<vector<char>>& board, s_iter begin, s_iter end, int x, int y)
    {
        if (!(0 <= x && x < board.size()) || !(0 <= y && y < board[0].size() || board[x][y] != *begin)
            return false;

        if (end - begin == 1)       // reached the end
            return true;
        
        board[x][y] = 0;            // mark so that we don't revisit

        if (explore(board, begin+1, end, x+1, y) || explore(board, begin+1, end, x-1, y)
                || explore(board, begin+1, end, x, y+1) || explore(board, begin+1, end, x, y-1)
            return true;
        
        board[x][y] = *begin;       // restore for next possible explore on new x, y
    }

    bool exist(vector<vector<char>>&board, string word)
    {
        for (int i = 0; i < board.size(); ++i)
            for (int j = 0; j < board[0].size(); ++j)
                if (board[i][j] == word[0] && explore(board, word.begin(), word.end(), i, j)
                    return true;
        return false;
    }
};
```

