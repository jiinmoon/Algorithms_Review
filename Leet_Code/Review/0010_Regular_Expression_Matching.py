""" 10. Regular Expression Matching

Question:

    Given a pattern involving wildcards '.' and '*', determine whether it
    matches the given text.

+++

Solution:

    Using the dynamic programming, we can find whether pattern matches the
    text. First, we need to define how DP[i][j] is going to be defined. Any
    arbitary index in text[i] and pattern[j] is a match if previous iteration
    have been also a match. But problem is the '*' character in the pattern
    where is can match 0 or more of the previous character. Hence, when we
    encounter '*', we need to check whether either is true: (1) we check for
    zero occurrences of previous pattern char, that is DP[i][j+2] or (2)
    current characters must match up and previous text while pattern char
    remains same.

"""

class Solution:
    def isMatch(self, text, pattern):
        m, n = len(text), len(pattern)
        dp = [[0] * (n+1) for _ in range(m+1]
        dp[-1][-1] = 1

        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                firstMatch = i < m and pattern[j] in {'.', text[i]}
                if j + 1 < n and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or firstMatch and dp[i+1][j]
                else:
                    dp[i][j] = firstMatch and dp[i+1][j+1]
        return dp[0][0]


