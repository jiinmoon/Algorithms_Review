""" 10. Regular Expression Matching

Question:

    Given an input string and a pattern, implement regular expression matching
    with support for '.' and '*'.

+++

Solution:

    DP would be a preferable approach to this problem - we can define DP[i][j]
    as a match between string and pattern upto i (from string) and j (from
    pattern) indicies.

    Then, as we read on the string and pattern, we encounter two major cases:

    1) s[i] == p[j] or p[j] == '.':

    This is a matching case - for pattern, '.' matches any single char, thus it
    would also fall under matching case as well. Then, DP[i][j] depends on
    whether previous iteration has been a match: DP[i-1][j-1].

    2) p[j] == '*':

    If the current pattern is wildcard '*', then it would match zero or more of
    the preceding element - meaning that we will have to look behind further.
    First, we can check whether zero occurrence of the preceding element is the
    true - it is done by examining DP[i][j-2]. Or, we could also check for one
    or more matches of preceding element which is from DP[i-1][j]. Otherwise, it
    would be False.

"""

class Solution:
    def isMatch(self, text, pattern):
        m, n = len(text), len(pattern)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[-1][-1] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                first_match = i < m and pattern[j] in {text[i], '.'}
                if j + 1 < n and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
