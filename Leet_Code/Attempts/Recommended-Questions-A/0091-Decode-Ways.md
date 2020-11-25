# 91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of
ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

---

For each digit, we have two possible cases: either it can form a digit by
itself (is not '0') or it can form a number of two digits from 10 to 26. Hence,
we can define a subproblem of dynammic programming. Let us suppose that upto
i-th index of given string, dp at i represents a maximum number of ways to
decode it. Then there are two possibilities as we iterate on each index:

(1) Single sigit case:

If at current index, the digit is not '0', it can be encoded as a single digit.
dp at i is added from dp[i-1], which is previous maximum encoded value.

(2) Two digit case:

We take a look at previous substring from i-2 to i. If integer value
represented by this digit can form a value between 10 and 26, we have a valid
way of representing this substring as a two digit case. Thus, dp at i is added
from dp[i-2]. 

We can make further improve on space complexity as at every index, we only
require two variables dp[i-1] and dp[i-2].

Time complexity would be O(n) and space is O(1) if improvement is made.

---

Java: O(1) space dp approach;

```java

class Solution {

    public int numDecodings(String s)
    {
        if (s == null || s == "")
            return 0;

        int m = s.length();
        int prevPrev = 1;
        int prev = (s.charAt(0) == 0) ? 0 : 1;

        for (int i = 2; i < m + 1; i++)
        {
            int total = 0;

            if (s.charAt(i) != '0')
                total += prev;

            int twoChars = Integer.valueOf(s.substring(i-2, i));
            if (10 <= twoChars && twoChars <= 26)
                total += prevPrev;

            prevPrev = prev;
            prev = total;
        }

        return prev;
    }
}

```

Java: 1-D dp array approach O(n) space;

```java

class Solution {

    public int numDecodings(String s)
    {
        if (s == null || s == "")
            return 0;

        int m = s.length();
        
        // dp[i] records max decodings upto i-th
        int[] dp = new int[m+1];

        dp[0] = 1;                              // base case
        dp[1] = (s.charAt(0) == '0') 0 : 1;     // can form two digit (0, 2)

        for (int i = 2; i < m + 1; i++)
        {
            char currChar = s.charAt(i-1);

            // single digit case
            if (currChar != '0')
                dp[i] += dp[i-1];

            // two digits case
            int currTwoChars = Integer.valueOf(s.substring(i-2, i));
            if (10 <= currTwoChars && currTwoChars <= 26)
                dp[i] += dp[i-2];
        }

        return dp[m];
    }
}

```
