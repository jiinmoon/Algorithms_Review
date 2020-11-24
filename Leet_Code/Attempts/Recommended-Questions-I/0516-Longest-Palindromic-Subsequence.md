# 516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You
may assume that the maximum length of s is 1000.

---

Naively, we may examine every subsequence size from 1 to length of s in order
to determine the longest palindromic subsequence.

Here, we can improve our time complexity to O(n^2) by utilizing the dynammic
programming.

Let's define dp[i][j] subproblem as a longest palindromic subsequence that we
have found thus far between string index from i to j (s[i:j]).

Then, we have following cases:

(1) i and j are equal; they are pointing at same character and by definition is
a base case of our palindrome; dp[i][j] is 1.

(2) char at i and j are equal; in this case, the current subsequence has been
increased by size of 2. The current subsequence follows from dp[i+1][j-1]. So,
dp[i][j] = dp[i+1][j-1] + 2.

(3) char at i and j are not equal; if so, the current subsequence value is the
maximum of the previous longest palindromic subsequence that we have seen thus
far which is either greater value from length of s[i+1:j] and s[i:j-1].

We can simplify this by recording only the maximum lengths that we have seen
thus far and consolidate it into a single dp array. For every starting
position, we iterate behind. Then, we only need an information about previous
substring examined at dp[i] before we update the dp array.

---

Java:


```java

class Solution {

    public int longestPalindromicSubseq(String s) {
        int m = s.length;
        int result = 0;
        int[] dp = new int[m];

        for (int i = 0; i < m; i++) {
            dp[i] = 1;      // substring of length 1
            result = 0;     // reset maximum length for current starting position
            // iterate to record each maximum
            for (int j = i - 1; j >= 0; j--) {
                int prev = dp[j];
                // new characters are same size + 2;
                if (s.charAt(i) == s.charAt(j))
                    dp[j] = 2 + result;
                result = Math.max(result, prev);
                }
            }
        }

        // find maximum length found thus far
        for (int i : dp)
            result = Math.max(i, result);

        return result;
    }
}

```
