# 72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

---

#### (1). Recursion with memoization.

We iterate on both of the strings to check the characters at each index. If
they are equal, then no editing is necessary and we can move on. Otherwise, we
have to exhaustively consider three cases of inserting, deleting and replacing
a character; and find the minimum amongst them + 1. As the edit distance is
fixed for each index, we can use memoization to save the result of the previous
iteration so that we do not have to recompute. This would be O(m * n) in time
complexity as we can avoid having to consider every possibilities and recompute
the edit distances.

#### (2). DP.

Another approach is to use dynammic programming which mirrors the idea from
above.

    Let DP[i][j] be minimum edit distance upto word1[:i] and word2[:j]. Then,
    consider following:

        (1) word1[i-1] == word2[j-1]

            In this case, two characters are equal and no editing is necessary.
            DP[i][j] can be updated from previous DP[i-1][j-1]

        (2) otherwise

            Characters are not same and we have to perform edition. We have to
            consider editing either of the strings or both. Since we have
            performed an edition here, we increase count by 1.

Time complexity would be O(m * n) and same for space complexity.

---

Python: DP.

```python

class Solution72:

    def minDistance(self, word1, word2):

        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # initialize first row and col;
        # have to edit upto m and n
        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            dp[0][i] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # no edit
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # editing; consider editing either word1 or word2 or both.
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
```

